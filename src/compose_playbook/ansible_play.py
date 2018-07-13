#!/usr/bin/python

import os
import sys
import fileinput

# Store the contents of brew play template in brew_play_template
# and required packages in brew_packages
brew_play_template= open("brew_play_template.yml","r").read()

brew_packages= open("/Users/nschhina/desktop/HomeBrew Package Manager/src/packages","r").read()
brew_packages_array=brew_packages.split()

num_packages = len(brew_packages.splitlines())

brew_playbook= open("brewplay.yml","a+")
brew_playbook.write(brew_play_template)

for i in range(num_packages):

    brew_playbook.write("      - " + brew_packages_array[i]+ "\n")
