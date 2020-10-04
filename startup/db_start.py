# *-* coding: utf-8 *-*

import requests
import datetime
from hashlib import md5
from mongo import MongoDB

try:
    print("Starting importing process.....")
    mongo_db = MongoDB(database_name='marvel', collection_name='character_info')
    data_in_db = mongo_db.get_all()
    if not data_in_db:
        START_URL = "https://gateway.marvel.com/v1/public/characters"
        PRIVATE_KEY = "0f56ea9eaad631cee9aed42478145bac470364fb"
        PUBLIC_KEY = "f455a0f7b332cf2db81353408eabae56"
        timestamp = str(datetime.datetime.now().timestamp())
        hash_ = timestamp + PRIVATE_KEY + PUBLIC_KEY
        params = {
            "ts": timestamp,
            "apikey": PUBLIC_KEY,
            "hash": md5(hash_.encode()).hexdigest()
        }
        print("Making request to  Marvel.....")
        request = requests.get(START_URL, params)

        if request.status_code == 200:
            response = request.json()
            print("Inserting results.....")
            for value in response["data"]["results"]:
                mongo_db.insert(value)
            print("Inserted " + str(len(response["data"]["results"])) + " results.")
        else:
            print("Something went wrong with Marvel API.....")
    else:
        print("DB already populated.")

except Exception as err:

    print("Something went wrong with the importing process.")
    print(err)
