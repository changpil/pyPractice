import json, requests, time
from requests.auth import HTTPBasicAuth

from skytap_api.CONSTANTS import *


class Skytap:
    def __init__(self, version):
        if version == 'v1':
            self.headers = {'content-type': 'application/json', 'accept': 'application/json'}
            self.url = SKYTAP_URL
        elif version == 'v2':
            self.headers = {'content-type': 'application/json', 'accept': 'application/vnd.skytap.api.v2+json'}
            self.url = SKYTAP_URL + version + "/"
        else:
            raise ValueError("Currently api supports V1 and v2 version: you entered {}".format(version))
        self.version = version
        self.auth = HTTPBasicAuth(CREDENTIAL["username"],CREDENTIAL["token"])
        self._update_environment()

    def _update_environment(self):
        """
        Get updatd status and VMs
        :return:
        """
        self.env = None
        if self.version == "v2":
            for env in self._get_contents(verb="GET", path="configurations"):
                if env["name"] == ENVIRONMENT_NAME:
                    self.env = env.copy()
        else:
            for id in self._get_contents(verb="GET", path="configurations"):
                env = self._get_contents(verb="GET", path="configurations/" + id["id"] +".json")
                if env["name"] == ENVIRONMENT_NAME:
                    self.env = env.copy()
        if self.env == None:
            raise Exception("{} does not exist as a name of environment".format(ENVIRONMENT_NAME))

    def _get_contents(self, verb="GET", path=None, payload=None):
        """
        This function sends api requests. If a server is busy, this function continues to try until timeout reaches MAX_WAIT_TIME
        :param verb: GET, PUT
        :param path: extra url
        :param payload: for params for PUT verb
        :return:
        """
        if path == None:
            raise ValueError("get_content needs path after {}".format(self.url))
        url = self.url + path
        sleeptime = 20
        while sleeptime < MAX_WAIT_TIME:
            response = requests.request(verb, url=url, auth=self.auth, headers=self.headers, params=payload)
            if response.status_code >= 500:
                raise Exception('[!] [{0}] Server Error'.format(response.status_code))
            # V1, V2 The operation could not be completed because the resource was busy. Try again in a few moments.
            elif response.status_code == 422 or response.status_code == 423:
                print("server is busy. wait ...")
                time.sleep(sleeptime)
                sleeptime *= 1.5
                continue
            elif response.status_code == 404:
                raise Exception('[!] [{0}] URL not found: [{1}]'.format(response.status_code,url))
            elif response.status_code == 401:
                raise Exception('[!] [{0}] Authentication Failed'.format(response.status_code))
            elif response.status_code == 400:
                raise Exception('[!] [{0}] Bad Request'.format(response.status_code))
            elif response.status_code >= 300:
                raise Exception('[!] [{0}] Unexpected Redirect'.format(response.status_code))
            elif response.status_code == 200:
                try:
                    contents = json.loads(response.content.decode('utf-8'))
                except:
                    raise Exception("The api request returned html format or corrupted json")
                return contents
            else:
                raise Exception('[?] Unexpected Error: [HTTP {0}]: Content: {1}'.format(response.status_code, response.content))

    def change_env_status(self, status):
        """
        Change status of environment and wait until this process is done
        :param status: running, reset, stopped, halted, suspended
        :return:
        """
        if len(self.env["vms"]) == 0:
            raise Exception("No avilable VMs in {} environment".format(ENVIRONMENT_NAME))
        payload = {"runstate": status}
        self._get_contents(verb="PUT", path="configurations/" + self.env["id"] + ".json", payload=payload)
        self._wait_for_busy_state()
        return self.env["runstate"]

    def is_env_status(self, status):
        """
        check if environment runstate is the state variable
        :param status: running, stopped, suspended, busy
        :return:
        """
        self._update_environment()
        return self.env["runstate"] == status

    def is_env_busy(self):
        """
        check if environment runstate is busy
        :return:
        """
        self._update_environment()
        return self.is_env_status("busy")

    def _get_all_vms(self):
        """
        return list of VMs
        :return:
        """
        self._update_environment()
        return self.env["vms"]

    def change_all_vms_status(self, state):
        """
        Change VMs' runstate in the environment
        :param status: running, reset, stopped, halted, suspended
        :return:
        """
        payload = {"runstate":state}
        for vm in self._get_all_vms():
            path = "configurations/" + str(self.env["id"]) + "/vms/" + str(vm["id"]) + ".json"
            self._get_contents(verb="PUT", path=path, payload=payload)
            print("... '{}' to '{}' state".format(vm["name"], state))
            self._wait_for_busy_state()

    def _select_vms_state1_to_state2(self, state1, state2):
        """
        Change VMs' runstate in the environment
        :param status: running, reset, stopped, halted, suspended
        :return:
        """
        self._wait_for_busy_state() # in case, web may be changing VM's state
        payload = {"runstate":state2}
        for vm in self._get_all_vms():
            if vm["runstate"] == state1:
                path = "configurations/" + str(self.env["id"]) + "/vms/" + str(vm["id"]) + ".json"
                self._get_contents(verb="PUT", path=path, payload=payload)
                print("... '{}' to '{}' state".format(vm["name"], state2))
                self._wait_for_busy_state()


    def _wait_for_busy_state(self):
        """
        This function can wait busy state in the environment until timeout reaches MAX_WAIT_TIME
        :return:
        """
        sleeptime = 20
        print("server is busy. wait ...")
        time.sleep(sleeptime)
        while self.is_env_busy():
            print("server is busy. wait ...")
            time.sleep(sleeptime)
            if sleeptime > MAX_WAIT_TIME:
                raise Exception("Server Error: busy state is more than max_wait_time {}".format(MAX_WAIT_TIME))
            sleeptime *= 1.5

    def is_all_vms_status(self, status):
        """
        Check if all VMs in the environment are same run state
        :param status:
        :return:
        """
        if len(self.env["vms"]) == 0:
            return False
        for vm in self._get_all_vms():
            if vm["runstate"] != status:
                return False
        return True

    def run_environment(self):
        """
        Try to start VMs in the entire environment, but the vms/environment will remain in the previous state if any of the vms fails to start.
        If environment start has any failure, then try to start individual VMs so that environment state can be "running" state.
        Even if at keast Pattern1:knapsack VM is running, environment is "running" state. Therefore, even if env runstate is running, let's try to run alll VMs.
        :return:
        """
        if self.change_env_status("running") != "running":  # all or nothing
            self.change_all_vms_status("running")
        if not self.is_env_status("running"):
            raise Exception("Environment cannnot start: check your VMs")

    def suspend_environment(self):
        """
        Try to suspend VMs in the entire environment, but the vms/environment will remain in the previous state if any of the vms fails to suspend.
        If environment suspend has any failure, then try to suspend individual VMs so that environment state can be "suspended" state.
        :return:
        """
        if self.is_env_status("suspended"):
            return
        if self.is_env_status("stopped"): # do not support "stoppped" stage to "suspended" state
            return
        if self.change_env_status("suspended") != "suspended":  # all or nothing
            self._select_vms_state1_to_state2("running","suspended")
        if not self.is_env_status("suspended"):
            raise Exception("Environment cannnot be suspended: check your VMs")


    def resume_environment(self):
        """
        Try to resume suspened VMs in the entire environment. If there are stopped VMs in environment, leave them to "stopped".
        if VMs are mixed with stopped and suspended VMs, environment runstate shows "suspended" unless there is a VM as "running" state.
        If there are only stopped VMs in the environment, environment runstate will be stoppped continously.
        :return:
        """
        self._select_vms_state1_to_state2("suspended", "running")
        if self.is_env_status("suspended"):
            raise Exception("Environment cannnot resume from suspended state")


    def poweroff_environment(self):
        """
        Try to poweroff VMs in the entire environment.
        If environment poweroff has any failure from "grace shutdown", then try to power off from the forced shutdown.
        :return:
        """
        if self.is_env_status("stopped"):
            return
        if self.change_env_status("stopped") != "stopped":
            self.change_env_status("halted")
        if not self.is_env_status("stopped"):
            raise Exception("Environment cannnot poweroff")

#skytap = Skytap("v2")
#skytap.run_environment()
#skytap.suspend_environment()
#skytap.resume_environment()
#skytap.poweroff_environment()