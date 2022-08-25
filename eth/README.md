# Ethereum Node Scripts
This is a collection of scripts to demonstrate how Ethereum Node Infrastructure works in [Coinbase Cloud](https://www.coinbase.com/cloud). The included Native API scripts work for both shared and dedicated nodes. The Advanced Query APIs are available only on the shared node product at this time.

# Script Parameters:
* `AccountAddress`: The public address of the entity
* `ContractAddress`: The address of the smart contract for the token
* `TransactionHash`: The hash address for the transaction on the block
* Block Range: Several APIs expect the block range determined by:
  * `BlockStart`: the first block in the range
  * `BlockEnd`: the last block in the range
  
__Note: All Block Range inputs are in Hex Encoding__


# Script Information and Example
## Native API Scripts
### [get_block_info.py](../../main/eth/native-apis/get_block_info.py)
  * Input: N/A
  * Description: Retrieves the latest block number and displays information on the block
```py
python native-apis/get_block_info.py
```
### [get_transaction.py](../../main/eth/native-apis/get_transaction.py) 
  * Inputs: TransactionHash 
  * Description: Retrieves specific information on a transaction given its hash
 ```py
 python native-apis/get_transaction.py 0x4859460fcc828c0fd0d3b34ddf86bd4666ebf2e953065ef5b537dbb6eec3a264
 ```

## Advanced API Scripts
### [get_balances.py](../../main/eth/advanced-apis/get_balances.py) 
  * Input: AccountAddress
  * Description: Retrieves the ETH, USDT, USDC, MATIC balances for the given account address. 
```py
python advanced-apis/get_balances.py 0x742d35Cc6634C0532925a3b844Bc454e4438f44e
```
### [get_single_balance.py](../../main/eth/advanced-apis/get_single_balance.py) 
  * Inputs: AccountAddress ContractAddress  
  * Description: Retrieves the balance for the account address given of the token specified by the contract address
```py
python advanced-apis/get_single_balance.py 0x742d35Cc6634C0532925a3b844Bc454e4438f44e 
```
### [get_token_metadata.py](../../main/eth/advanced-apis/get_token_metadata.py) 
  * Input: ContractAddress 
  * Description: Retrieves the metadata for the token specified by the contract address provided
```py
python advanced-apis/get_token_metadata.py 0xdac17f958d2ee523a2206206994597c13d831ec7
```

### [get_token_standard_events.py](../../main/eth/advanced-apis/advanced-apis/get_token_standard_events.py) 
  * Inputs: ContractAddress BlockStart BlockEnd 
  * Description: Returns the token events within the specified block range
```py
python advanced-apis/get_token_standard_events.py 0xdac17f958d2ee523a2206206994597c13d831ec7 0xeb11aa 0xeb11ac
``` 

### [get_token_transfers_by_address.py](../../main/eth/advanced-apis/get_token_transfers_by_address.py) 
  * Inputs: AccountAddress BlockStart BlockEnd
  * Description: Pulls all token transfers for the account address within the given block range
```py 
python advanced-apis/get_token_transfers_by_address.py 0x742d35Cc6634C0532925a3b844Bc454e4438f44e 0xeb11aa 0xeb11ac
``` 

### [get_transaction_by_hash.py](../../main/eth/advanced-apis/get_transaction_by_hash.py) 
  * Input: TransactionHash 
  * Description: Retrieves transaction metadata given its hash
```py
python advanced-apis/get_transaction_by_hash.py 0x4859460fcc828c0fd0d3b34ddf86bd4666ebf2e953065ef5b537dbb6eec3a264
``` 

### [get_transactions_by_address.py](../../main/eth/advanced-apis/get_transactions_by_address.py) 
  * Inputs: AccountAddress BlockStart BlockEnd 
  * Description: Gets all transactions for an account within the specified block range
```py 
python advanced-apis/get_transactions_by_address.py 0x742d35Cc6634C0532925a3b844Bc454e4438f44e 0xeb11aa 0xeb11ac
```
