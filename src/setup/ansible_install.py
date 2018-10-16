import subprocess
import platform

def pipinstaller():
    if(platform.system()=='Darwin'):
        pip_install_command = 'sudo easy_install pip'
        subprocess.check_call(pip_install_command.split())
        nose_install_command = 'sudo easy_install nose'
        subprocess.check_call(nose_install_command.split())
        tornado_install_command = 'sudo easy_install tornado'
        subprocess.check_call(tornado_install_command.split())


def ansibleinstaller():
    pip_install_ansible = 'pip install ansible'
    subprocess.check_call(pip_install_ansible.split())
    pip_upgrade_ansible = 'pip install ansible --upgrade --quiet'
    subprocess.check_call(pip_upgrade_ansible.split())
