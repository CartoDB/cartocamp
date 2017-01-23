import json

# modify credentials.json.sample
cred = json.load(open('credentials.json'))

username = cred['username']
api_key  = cred['api_key']

print username