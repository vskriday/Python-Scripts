#! /usr/bin/python3
import requests
from web3 import Web3,HTTPProvider

def main():
web3 = Web3(HTTPProvider("http://localhost:8546"))
geth_latestBlock = web3.eth.blockNumber
print ('ethereum mainnet latest blocks in Decimal :',a )

etherscan_web3 = requests.get('https://api.etherscan.io/api?module=proxy&action=eth_blockNumber&apikey=api_token')
eth_block = etherscan_web3.json()
eth_block_latest = eth_block['result']

eth_block_latestInDecimal = int("{}".format(eth_block_latest), 16)
print ("latest blocks from etherscan.io in Decimal:", eth_block_latestInDecimal)

if geth_latestBlock == eth_block_latestInDecimal:
  print ("Block syncing is working fine")
else: 
  print("Something went wrong!")


if __name__ == "__main__":
print ("Script is running...")
main()
print ("Script end")