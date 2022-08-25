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

import json, os, requests, web3

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

# Create a session with username and password
session = requests.Session()
session.auth = (NODE_USERNAME, NODE_PASSWORD)

# Connect to your Node
w3 = web3.Web3(web3.Web3.HTTPProvider(NODE_ENDPOINT, session=session))

# Get latest block
latest_block = w3.eth.block_number
print('Latest Ethereum Block is: \n', latest_block)

# Get info about block
block_json = json.dumps(
  json.loads(w3.toJSON(w3.eth.get_block(latest_block))),
  indent=3)
print('Information about block: \n', block_json)