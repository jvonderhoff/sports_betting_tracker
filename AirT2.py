import requests

base_id = "appnN7BwmXQR0uOSW"
table_name = "Teams"
url = "https://api.airtable.com/v0/" + base_id + "/" + table_name  

api_key = "keyeAXy0jPNEOdZJR"

headers = {"Authorization": "Bearer {}".format(api_key)}



params = ()
airtable_records = []
run = True
while run is True:
  response = requests.get(url, params=params, headers=headers)
  airtable_response = response.json()
  airtable_records += (airtable_response['records'])
  if 'offset' in airtable_response:
     run = True
     params = (('offset', airtable_response['offset']),) + constant_params
  else:
     run = False

response = requests.get(url, params=params, headers=headers)
airtable_response = response.json()

airtable_records = airtable_response['records']



print(airtable_records)
