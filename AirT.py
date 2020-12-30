import requests
from airtable import Airtable
import json

base_key = 'appnN7BwmXQR0uOSW'
table_name = 'Teams'
api_key = 'keyeAXy0jPNEOdZJR'

airtable = Airtable(base_key, table_name, api_key)

records = airtable.get_all(fields='Team')

print(records)

