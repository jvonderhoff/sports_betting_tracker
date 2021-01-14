# create an airtable record
import logging
import os
import sys
from urllib import parse
import requests


logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


BASE_URL = "https://api.airtable.com/v0"
class AirtableClient:
    def __init__(self, apikey, basekey):
        self.apikey = apikey
        self.basekey = basekey

    def __headers(self):
        return {"Authorization": f"Bearer {self.apikey}"}
    
    def insert_airtable_rec(self, table_name, records):
        """
        insert a betting record (currently takes only spread)
        """        

        if(len(records) != 10):
            logger.info({f"Record is incomplete. Array size is less than or greter than 10"})
            return 
        

        #TODO: grab the fields from the table or a config file and loop over instead of listed out
        rec = {
            "Sport": records[0],
            "Status": records[9],
            "League": records[1],
            "Date": "2020-12-30",
            "Bet Type": records[5],
            "Team 1": records[2],
            "Team 2": records[3],
            "Betting Team": records[4],
            "Platform": records[8],
            "Bet Odds":  int(records[7]),
            "Spread": records[6],           
        }

        data = {"records": []}
        data["records"].append({"fields": rec})    

        url = os.path.join(BASE_URL, self.basekey, parse.quote(table_name))
        response = requests.post(url, json=data, headers=self.__headers()) 
        print(response)
        return response
    

