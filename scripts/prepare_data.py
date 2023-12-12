import os
import requests
import hashlib

data_url = "https://archive.ics.uci.edu/dataset/19/car+evaluation"
response_reconstruction = requests.get(data_url)
with open('/Users/victordashuaibi/Desktop/is477-fall2023-final-project/data/car.csv', mode='wb') as f:
    f.write(response_reconstruction.content)

filename = '/Users/victordashuaibi/Desktop/is477-fall2023-final-project/data/car.csv'
with open (filename, mode='rb') as f:
    data = f.read()
    sha256hash = hashlib.sha256 (data).hexdigest ()

data_sha256 = 'b703a9ac69f11e64ce8c223c0a40de4d2e9d769f7fb20be5f8f2e8a619893d83'

if data_sha256 != sha256hash:
    print ("Computed hash does not match expected hash for original Car data")
else:
    print ("Computed hash matches expected hash for original Car data")

