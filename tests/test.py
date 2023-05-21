
def test_system_type(host):
    assert host.system_info.type == "linux"

def test_system_dist(host):
    assert host.system_info.distribution in ["ubuntu", "debian", "redhat", "centos", "rocky"]
    assert host.system_info.arch == 'x86_64' 

def test_user(host):
    assert host.user("sshd").exists

def test_ssh_config(host):
    ssh_config = host.file("/etc/ssh/ssh_config")
    assert ssh_config.user == "root"
    assert ssh_config.group == "root" 
    assert ssh_config.mode == 0o644

def test_sshd_config(host):
    sshd_config = host.file("/etc/ssh/sshd_config")
    assert sshd_config.user == "root"
    assert sshd_config.group == "root" 
    assert sshd_config.mode == 0o600

def test_sshd_installed(host):
    sshd = host.package("openssh-server")
    assert sshd.is_installed

def test_sshd_running_and_enabled(host):
    sshd = host.service("sshd")
    assert sshd.is_running
    assert sshd.is_enabled

def test_sshd_socket(host):
    sshd_v4 = host.socket("tcp://22")
    sshd_v6 = host.socket("tcp://:::22")
    assert sshd_v4.is_listening
    assert sshd_v6.is_listening