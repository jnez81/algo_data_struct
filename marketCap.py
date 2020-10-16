# Aggregation pipeline statement that determines a user-specified 
# company's market cap value.  Company specific stock information is 
# retrieved from MongoDB database "market" in the collection "stocks" 

import json 
from bson import json_util
from pymongo import MongoClient

client = MongoClient('localhost', 27017)
db = client.market
coll = db['stocks']

def aggregate():
    try: 
        
        # User-input company name to retrieve market cap value
        company = input('Enter company name using quotation marks: ')

        # Aggregation pipeline that identifies company name and multiplies company's
        # share price and shares outstanding value to determine company's market cap value
        pipe1 = [
                {'$match': {"Company" : company}}, 
                {'$project': {"Company": 1, "Market Cap Value": { '$multiply': ["$Price", "$Shares Outstanding"] }}} 
              ]
        
        result = db.stocks.aggregate(pipe1)
        
        for x in result:
            print(x)
          
        
    except Exception as exception:
        print("Exception: {}".format(type(exception).__name__))
        print("Exception message: Use quotation marks and/or check spelling.")
        
aggregate()
