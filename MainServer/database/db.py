import ssl
from pymongo import MongoClient, DESCENDING
from MainServer.database.OtherFun import *
from MainServer.database.schemas import *
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()
# Access the environment variables
# DB_URL = os.getenv("DB_URL")
DB_URL = "mongodb+srv://dhruv20345:abxy123@cluster0.9bjdlnv.mongodb.net"
# Adding, not adding the security by Secure Socket Layer
# Create a MongoDB client with SSL certificate verification disabled
client = MongoClient(DB_URL, ssl_cert_reqs=ssl.CERT_NONE)

# Print a message to indicate successful connection
print("Connected successfully")

# Access the "SellerApp" database
db = client["SellerApp"]

# Access collections within the database
auctionCollection = db["auctionCollection"]
endedAuctionCollection = db["endedAuctionCollection"]
bidCollection = db["bidCollection"]
users = db["users"]
