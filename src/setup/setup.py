#!/usr/bin/python
import homebrew_install
import ansible_install
import sys


def main():
    homebrew_install.homebrewinstaller()
    print("installed Homebrew")
    ansible_install.pipinstaller()
    print("installed Pip")
    ansible_install.ansibleinstaller()
    print("installed Ansible")


if __name__ == "__main__":
    main()
