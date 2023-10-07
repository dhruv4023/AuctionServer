import ssl
from pymongo import MongoClient ,DESCENDING
from  MainServer.database.OtherFun import *
from  MainServer.database.schemas import *
import os
from dotenv import load_dotenv
load_dotenv()
# Load environment variables from .env file

# Access the environment variables
DB_URL = os.getenv("DB_URL")
# adding not adding the security by Secure Socket Layer
client = MongoClient(DB_URL, ssl_cert_reqs=ssl.CERT_NONE)


print("connected successfully")

db = client["SellerApp"]

# all collections
auctionCollection = db["auctionCollection"]
endedAuctionCollection = db["endedAuctionCollection"]
bidCollection = db["bidCollection"]
users = db["users"]