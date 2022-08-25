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

if len(sys.argv) != 4:
  print('Invalid Arguments: Expected AccountAddress BlockStart BlockEnd')
  print('Received: ', sys.argv[1:])
  print(exit(1))

account_address = sys.argv[1]
block_start = sys.argv[2]
block_end = sys.argv[3]

body = {
    'method': 'coinbaseCloud_getTransactionsByAddress',
    'id': 1,
    'jsonrpc': '2.0',
    'params': [
       account_address,
       block_start,
       block_end,
       'SENDER_OR_RECEIVER',
       'Ethereum',
       'Mainnet'
        ]
}

print(json.dumps(json.loads(requests.post(NODE_ENDPOINT, json=body, headers=headers).text), indent=3))
