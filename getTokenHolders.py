import requests
import json
import os
from dotenv import load_dotenv
load_dotenv()

TokenAddress = os.getenv("TokenAddress")
Chain = os.getenv("Chain")

url = 'https://rpc.ankr.com/multichain/569ca1f392f7d3d0bb1073a1173ecb649af1d9249231fe59fa95db19d5ae41fe/?ankr_getTokenHolders='
headers = {
    'accept': 'application/json',
    'content-type': 'application/json'
}
payload = {
    'jsonrpc': '2.0',
    'method': 'ankr_getTokenHolders',
    'params': {
        'blockchain': Chain,
        'contractAddress': TokenAddress
    },
    'id': 1
}

response = requests.post(url, headers=headers, data=json.dumps(payload))
data = response.json()

holders = data['result']['holders']
next_page_token = data['result'].get('nextPageToken')

all_holders = holders if holders else []

while next_page_token:
    payload['params']['pageToken'] = next_page_token
    response = requests.post(url, headers=headers, data=json.dumps(payload))
    data = response.json()
    holders = data['result']['holders']
    next_page_token = data['result'].get('nextPageToken')
    if holders:
        all_holders.extend(holders)

with open('holders.json', 'w') as file:
    json.dump(all_holders, file)

with open('holders.json', 'r') as file:
    holders_data = json.load(file)

holder_addresses = [holder['holderAddress'] for holder in holders_data]

with open('holder_addresses.txt', 'w') as file:
    for address in holder_addresses:
        file.write(address + '\n')