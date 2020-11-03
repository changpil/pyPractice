import pytest
from skytap_api.skytap import Skytap

@pytest.fixture
@pytest.mark.vms()
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

@pytest.mark.vms()
def test_invalid_VMs(skytap_stopped):
    skytap_stopped.run_environment()
    assert skytap_stopped.is_all_vms_status("running")