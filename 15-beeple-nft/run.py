# Christie's Beeple auction page: https://onlineonly.christies.com/s/beeple-first-5000-days/beeple-b-1981-1/112924

import requests,json,wget,os
from web3 import Web3

infura_api_key = os.getenv('INFURA_API_KEY') #'940b268eaee746c7a4f9402b6bb7a7bc'
etherscan_api_key = os.getenv('ETHERSCAN_API_KEY') #'S3AXP8WGI4NI4U4HDGI29BVFP9E8QNI6QC'

w3 = Web3(Web3.HTTPProvider(f'https://mainnet.infura.io/v3/{infura_api_key}'))

sca = '0x2A46f2fFD99e19a89476E2f62270e0a35bBf0756'
abi = requests.get(f'https://api.etherscan.io/api?module=contract&action=getabi&address={sca}&apikey={etherscan_api_key}').json()
abi = json.loads(abi['result'])

beeple_token_id = 40913 # As per Christie's website
contract = w3.eth.contract(address=sca,abi=abi)
ipfs_url = contract.functions.tokenURI().call()
ipfs_id = ipfs_url.split('/')[3]
ipfs_meta_url = f'https://ipfsgateway.makersplace.com/ipfs/{ipfs_id}'
ipfs_image_url = requests.get(ipfs_meta_url).json()['imageUrl']

wget.download(ipfs_image_url,out='beeple.jpg')

# Extra credit: Get transaction info
# tx = '0xa342e9de61c34900883218fe52bc9931daa1a10b6f48c506f2253c279b15e5bf'
# print(w3.eth.get_transaction(tx))
