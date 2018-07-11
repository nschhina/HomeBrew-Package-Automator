import subprocess
pip_install_command = 'sudo easy_install pip'
subprocess.check_call(pip_install_command.split())
pip_install_ansible = 'sudo pip install ansible --quiet'
subprocess.check_call(pip_install_ansible.split())
pip_upgrade_ansible = 'sudo pip install ansible --upgrade --quiet'
subprocess.check_call(pip_upgrade_ansible.split())