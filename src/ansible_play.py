#!/usr/bin/python
import os
import json
import shutil
from collections import namedtuple
from ansible.parsing.dataloader import DataLoader
from ansible.vars.manager import VariableManager
from ansible.inventory.manager import InventoryManager
from ansible.playbook.play import Play
from ansible.executor.task_queue_manager import TaskQueueManager
from ansible.plugins.callback import CallbackBase
import ansible.constants as C

class ResultCallback(CallbackBase):

  def v2_runner_on_ok(self, result, **kwargs):
    host = result._host
    print json.dumps({host.name: result._result}, indent=4)

#Options = namedtuple('Options', ['connection', 'module_path', 'forks', 'become', 'become_method', 'become_user', 'check'])
loader = DataLoader()
Options = namedtuple('Options', ['connection', 'module_path', 'forks', 'become', 'become_method', 'become_user', 'check', 'diff'])
options = Options(connection='local', module_path=['/usr/share/ansible/plugins/modules'], forks=10, become=None, become_method=None, become_user=None, check=False, diff=False)
passwords = "hi"

results_callback = ResultCallback()

inventory = InventoryManager(loader=loader, sources='172.16.10.12,')
variable_manager = VariableManager()
variable_manager.set_inventory(inventory)

play_source =  dict(
        name = "Ansible Play",
        hosts = 'localhost',
        gather_facts = 'no',
        tasks = [
            dict(action=dict(module='shell', args='ls'), register='shell_out'),
         ]
    )
play = Play().load(play_source, variable_manager=variable_manager, loader=loader)



tqm = None
try:
    tqm = TaskQueueManager(
              inventory=inventory,
              variable_manager=VariableManager(),
              loader=loader,
              options=options,
              passwords=passwords,
              stdout_callback= results_callback,  # Use our custom callback instead of the ``default`` callback plugin
          )
    result = tqm.run(play)
finally:
    if tqm is not None:
        tqm.cleanup()
    shutil.rmtree(C.DEFAULT_LOCAL_TMP, True)
