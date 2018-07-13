#!/usr/bin/python
import os
import sys

sys.path.append('compose_playbook')
from compose_playbook import write_playbook
sys.path.append('runner_playbook')
from exec_playbook import exec_playbook

def main():
    write_playbook()
    exec_playbook()
    os.remove("brewplay.yml")


if __name__ == "__main__":
    main()
