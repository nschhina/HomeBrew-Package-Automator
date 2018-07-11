import subprocess
ruby_install_brew = 'sudo Yes | ruby -e "$( curl --silent -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"'
brew_install_cask = 'brew install caskroom/cask/brew-cask'
subprocess.check_call(brew_install_cask.split())
