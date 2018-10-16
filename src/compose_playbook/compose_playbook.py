#!/usr/bin/python

import os
import sys
import fileinput
import platform
import os.path
sys.path.append(os.path.dirname(os.path.dirname(__file__)))
# Store the contents of brew play template in brew_play_template
# and required packages in brew_packages
def write_playbook():
        # Set necessarily file variables pointing to the template files
        brew_play_template= open("compose_playbook/brew_play_template.yml","r").read()
        linux_play_template= open("compose_playbook/linux_play_template.yml","r").read()
        windows_play_template= open("compose_playbook/windows_play_template.yml","r").read()

        # Read the packages file into brew_packages
        brew_packages= open("packages","r").read()
        # Split all the packages defined and store them in a list
        brew_packages_array=brew_packages.split()

        # Set number of packages by counting the number of lines in the packages file
        num_packages = len(brew_packages.splitlines())

        #check if brewfile/packagefile exist in current dir, if yes remove them(remove cache if exists)
        if os.path.exists("brewfile.yml"):
            os.remove("brewfile.yml")

        if os.path.exists("packagefile.yml"):
            os.remove("packagefile.yml")

        #Create appropriate playbook for the current OS

        # If current OS is Mac
        if platform.system()=='Darwin':
            brew_playbook= open("brewplay.yml","a+")
            brew_playbook.write(brew_play_template)

        # If current OS is Linux
        elif platform.system()=='Linux':
            brew_playbook= open("packageplay.yml","a+")
            brew_playbook.write(linux_play_template)

        # If current OS is windows
        elif platform.system()=='Windows':
            brew_playbook= open("winplay.yml","a+")
            brew_playbook.write(windows_play_template)

        # Write all the packages wanted onto "with items argument of packages/brew module"
        for i in range(num_packages):
            brew_playbook.write("      - " + brew_packages_array[i]+ "\n")
