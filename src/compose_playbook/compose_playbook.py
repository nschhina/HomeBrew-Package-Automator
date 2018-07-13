#!/usr/bin/python

import os
import sys
import fileinput
import os.path

# Store the contents of brew play template in brew_play_template
# and required packages in brew_packages
def write_playbook():
        brew_play_template= open("compose_playbook/brew_play_template.yml","r").read()

        brew_packages= open("packages","r").read()
        brew_packages_array=brew_packages.split()

        num_packages = len(brew_packages.splitlines())

        if os.path.exists("brewfile.yml"):
            os.remove("brewfile.yml")

        brew_playbook= open("brewplay.yml","a+")
        brew_playbook.write(brew_play_template)

        for i in range(num_packages):
            brew_playbook.write("      - " + brew_packages_array[i]+ "\n")
