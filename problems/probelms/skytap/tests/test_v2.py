import pytest
from skytap_api.skytap import Skytap

@pytest.fixture
@pytest.mark.v2()
def skytap_stopped(request):
    """
    Target: v2 api
    This is pre-stage before an VMs test runs.
    If this stage is not met "stopped" runstate, skip a test
    :param request:
    :return:
    """
    skytap = Skytap(version="v2")
    try:
        skytap.poweroff_environment()
    except:
        pytest.skip("Environment cannot be set to 'stoppped runstate'")
    def poweroff_env():
        skytap.poweroff_environment()
    request.addfinalizer(poweroff_env)
    return skytap

@pytest.fixture
@pytest.mark.v2()
def skytap_suspended(request):
    """
    Target: v2 api
    This is pre-stage before an VMs test runs.
    If this stage is not met "suspended" runstate, skip a test
    :param request:
    :return:
    """
    skytap = Skytap(version="v2")
    try:
        skytap.run_environment()
        skytap.suspend_environment()
    except:
        pytest.skip("Environment cannot be set to 'suspended runstate'")
    def poweroff_env():
        skytap.poweroff_environment()
    request.addfinalizer(poweroff_env)
    return skytap

@pytest.fixture
@pytest.mark.v2()
def skytap_running(request):
    """
    Target: v2 api
    This is pre-stage before an VMs test runs.
    If this stage is not met "running" runstate, skip a test
    :param request:
    :return:
    """
    skytap = Skytap(version="v2")
    try:
        skytap.run_environment()
    except:
        pytest.skip("Environment cannot be set to 'running runstate'")
    def poweroff_env():
        skytap.poweroff_environment()
    request.addfinalizer(poweroff_env)
    return skytap

@pytest.mark.v2()
def test_run_environment_from_stopped(skytap_stopped):
    """
    change environment from stopped to running
    :param skytap_stopped:
    :return:
    """
    skytap_stopped.run_environment()
    assert skytap_stopped.is_env_status("running")

@pytest.mark.v2()
def test_run_environment_from_suspended(skytap_suspended):
    """
    change environment from suspended to running
    :param skytap_suspended:
    :return:
    """
    skytap_suspended.run_environment()
    assert skytap_suspended.is_env_status("running")

@pytest.mark.v2()
def test_suspend_environment_from_running(skytap_running):
    """
    change environment from running to suspended
    :param skytap_running:
    :return:
    """
    skytap_running.suspend_environment()
    assert skytap_running.is_env_status("suspended")

@pytest.mark.v2()
def test_poweroff_environment_from_running(skytap_running):
    """
    change environment from running to stopped
    :param skytap_running:
    :return:
    """
    skytap_running.poweroff_environment()
    assert skytap_running.is_env_status("stopped")

@pytest.mark.v2()
def test_poweroff_environment_from_suspended(skytap_suspended):
    """
    change environment from suspended to stopped
    :param skytap_suspended:
    :return:
    """
    skytap_suspended.poweroff_environment()
    assert skytap_suspended.is_env_status("stopped")
