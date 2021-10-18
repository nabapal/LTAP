#!/usr/bin/env python3
import json
import requests
api_key = "2a84465a-cf38-46b2-9d86-b84Q7d57f288"
api_url_base = "http://10.49.11.150:65101"
headers = {
    "Content-Type": "application/json",
    #'Authorization': 'Bearer {0}'.format(api_token)
    "x-api-key": api_key,
}

def napalm_setconfig_j2(payload):
    api_url = api_url_base + "/setconfig"
    response = requests.post(api_url, headers=headers, data = json.dumps(payload))
    if response.status_code == 201:
        return json.loads(response.content.decode("utf-8"))
    else:
        return None

def task(task_id):
    api_url = api_url_base + "/task/" + task_id
    response = requests.get(api_url, headers=headers)
    if response.status_code == 200:
        return json.loads(response.content.decode("utf-8"))
    else:
        return None
def getconfig(payload):
    payload = payload
    api_url = api_url_base + "/getconfig"
    response = requests.post(api_url, headers=headers, data = json.dumps(payload))
    if response.status_code == 201:
        return json.loads(response.content.decode("utf-8"))
    else:
        return None