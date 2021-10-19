from netpalmapi import getconfig, task
from pprint import pprint
from tabulate import tabulate
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
config = getconfig(payload)
task_id = config["data"]["task_id"]
result = task(task_id)
while result["data"]["task_status"] != "finished":
            result = task(task_id)
            #print (result)
            if result["data"]["task_status"] == "finished":
                break
hostname= result['data']['task_result']['get_facts']['hostname']
model = result['data']['task_result']['get_facts']['model']
serial_number= result['data']['task_result']['get_facts']['serial_number']
os_version = result['data']['task_result']['get_facts']['os_version']

devices = {
  "hostname": hostname,
  "model": model,
  "serial_number": serial_number,
  "os_version": os_version
}
print (devices)
#print(tabulate(devices, headers=["hostname", "model", "SL No", "OS"]))