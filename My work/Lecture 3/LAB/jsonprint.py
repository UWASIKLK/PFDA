# program to print the JSON file
# Author: Katarina Siklodyova

import requests

url = "https://api.coindesk.com/v1/bpi/currentprice.json"
response = requests.get(url)
data = response.json()
print (data)

print (data['bpi']['EUR']['rate_float'])
