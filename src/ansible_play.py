#!/usr/bin/python

import os
import sys
import fileinput

# Store the contents of brew play template in brew_play_template
# and required packages in brew_packages
brew_play_template= open("brew_play_template.yml","r").read()

brew_packages= open("packages","r").read()
brew_packages_array=brew_packages.split()

num_packages = len(brew_packages.splitlines())

brew_playbook= open("brewplay.yml","a+")

for i in range(num_packages):

    brew_playbook.write(brew_play_template.replace("foo", brew_packages_array[i]))
