import subprocess

def homebrewinstaller():
    ruby_install_brew = 'sudo echo "YES" | ruby -e "$( curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"'
    subprocess.Popen(ruby_install_brew,shell=True)
    brew_install_cask = 'brew install cask'
    subprocess.check_call(brew_install_cask.split())
