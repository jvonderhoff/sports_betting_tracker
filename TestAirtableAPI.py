import logging
import os
import sys
from AirtableAPI import AirtableClient

api_key = "key8khS01fFZYRQSv"
base_key = "appnN7BwmXQR0uOSW"
airtable_client = AirtableClient(api_key, base_key)

def Test_normal_insert_airtable_rec():
    rec = ["Football",
            "NFL",
            "Detroit Lions",
            "Greenbay Packer",
            "Greenbay Packer",
            "Spread",
            "+7",
            "-110",
            "Barstool",
            "Win"]
    ret = airtable_client.insert_airtable_rec("Bet History", rec)
    
    logging.info(ret)

def Test_incompleteList_insert_airtable_rec():
    rec = ["Football",
            "NFL",
            "Detroit Lions",
            "Greenbay Packer",
            "Greenbay Packer",
            "Spread",
            "-110",
            "Barstool",
            "Win"]
    ret = airtable_client.insert_airtable_rec("Bet History", rec)  
    if (ret == "Record is incomplete. Array size is less than or greter than 10") :
        logging.info("True")
    else :
        logging.info("False")

if __name__== "__main__":
    Test_normal_insert_airtable_rec()
    Test_incompleteList_insert_airtable_rec()

    

