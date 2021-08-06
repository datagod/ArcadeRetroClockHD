
import requests
import simplejson as json

url = "https://mainnet.infura.io/v3/b426370b8d7d4847b57db1b1a8603938"
data = {'jsonrpc':'2.0', 'id':1, 'method':'eth_getBalance', 'params':['0x3D15798193ecdc14217F431FC341fA81C70AAd45', 'latest']}
headers = {'Content-type': 'application/json'}
r = requests.post(url, data=json.dumps(data), headers=headers)

r_dict = json.loads(r.text)

print (r_dict)
print ("Etherbucks:",  int(r_dict['result'],0) / 1000000000000000000 * 728 * 1.30)

#print ("Etherbucks:",  bytearray.fromhex("r_dict[result]").decode() )
#print (r.text)
#print ("=============")