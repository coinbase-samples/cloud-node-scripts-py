# Copyright 2022 Coinbase Global, Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#   http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import base64, json, os, requests, sys

# Credentials
NODE_USERNAME = os.getenv('NODE_USERNAME')
NODE_PASSWORD = os.getenv('NODE_PASSWORD')
NODE_ENDPOINT = os.getenv('NODE_ENDPOINT')

if NODE_USERNAME is None or NODE_PASSWORD is None or NODE_ENDPOINT is None:
  print(f'''Missing required environment variables:\n
  NODE_USER: {NODE_USERNAME}\n
  NODE_PASSWORD: {NODE_PASSWORD}\n 
  NODE_ENDPOINT: {NODE_ENDPOINT}\n''')
  print(exit(1))

cred_str = f'{NODE_USERNAME}:{NODE_PASSWORD}'.encode('utf-8')
encoded_creds = base64.b64encode(cred_str).decode()
headers = {
    'Authorization': f'Basic {encoded_creds}',
    'Content-Type': 'application/json',
}

TOKEN_CONTRACT_LIST = [
  '0xdAC17F958D2ee523a2206206994597C13D831ec7', # USDT
  '0xA0b86991c6218b36c1d19D4a2e9Eb0cE3606eB48', # USDC
  '0x7D1AfA7B718fb893dB30A3aBc0Cfc608AaCfeBB0'  # MATIC
]

if len(sys.argv) != 2:
  print('Invalid Arguments: Expected AccountAddress')
  print('Received: ', sys.argv[1:])
  print(exit(1))

account_address = sys.argv[1]

get_balances_input = []

for token in TOKEN_CONTRACT_LIST:
  get_balances_input.append({
    "address": account_address,
    'contract': token
  })

body = {
    'method': 'coinbaseCloud_getBalances',
    'id': 1,
    'jsonrpc': '2.0',
    'params': {
        "addressAndContractList": get_balances_input,
        'blockchain': 'Ethereum',
        'network': 'Mainnet'
    }
}

print(json.dumps(json.loads(requests.post(NODE_ENDPOINT, json=body, headers=headers).text), indent=3))
