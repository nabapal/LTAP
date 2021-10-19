from netpalmapi import getconfig, task
from pprint import pprint
from tabulate import tabulate
import yaml


payload = {
  "library": "napalm",
  "connection_args": {
    "device_type": "cisco_ios",
    "host": "10.64.2.85",
    "username": "nabaa",
    "password": "Sept#@1234"
  },
  "command": "get_facts"
}
task_list = []
with open("devices.yaml", "r") as stream:
    try:
        devices = yaml.safe_load(stream)
    except yaml.YAMLError as exc:
        print(exc)
for device in devices['devices']:
  payload['connection_args']['host']= device['ip']
  payload['connection_args']['device_type'] = device['device_type']
  config = getconfig(payload)
  task_id = config["data"]["task_id"]
  task_list.append(task_id)
results =[]
for task_id in task_list:
  result = task(task_id)
  while result["data"]["task_status"] != "finished":
    result = task(task_id)
    if result["data"]["task_status"] == "finished":
      break
  results.append(result['data']['task_result']['get_facts'])
print("__HOSTNAME__","__MODEL__","__SERIAL_NUMBER__","__OS_VERSION__")  
for result in results:
  print(result['hostname'],result['model'],result['serial_number'],result['os_version'].split()[4])