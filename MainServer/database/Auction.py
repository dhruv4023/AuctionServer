from  MainServer.database.db import *
from  MainServer.database.Users import setUserName_and_id
from datetime import datetime

# Function to add a new auction
def add_new_auction(user_id: str, start_time: datetime, end_time: datetime, start_price: float, item_name: str, winner: str=""):
    # Create a dictionary with the provided parameters
    auction_data = {
        "start_time": start_time,
        "end_time": end_time,
        "start_price": float(start_price),
        "item_name": item_name,
        "created_by": user_id,
        "winner": winner,
        "bid_list": []
    }

    # Validate the auction data using a schema (AuctionSchema)
    validate_document(document=auction_data, schema=AuctionSchema)

    # Insert the auction data into the MongoDB collection
    result = auctionCollection.insert_one(auction_data)

    # Return the ID of the newly created auction
    return result.inserted_id

# Function to get all upcoming auctions
def get_upcoming_auctions(startIndex: int = 0, limit: int = 10):
    current_time = datetime.now()
    upcoming_auctions = auctionCollection.find({"start_time": {"$gt": current_time}},{"bid_list":0}).sort([("_id", DESCENDING)]).skip(startIndex).limit(limit)
    return convert_to_json(setUserName_and_id(list(upcoming_auctions), ["created_by"]))

# Function to get all currently ongoing auctions
def get_ongoing_auctions(startIndex: int = 0, limit: int = 10):
    current_time = datetime.now()
    ongoing_auctions = auctionCollection.find({"start_time": {"$lte": current_time}, "end_time": {"$gte": current_time}},{"bid_list":0}).sort([("_id", DESCENDING)]).skip(startIndex).limit(limit)
    return convert_to_json(setUserName_and_id(list(ongoing_auctions), ["created_by"]))

# Function to get all auctions created by a particular user
def get_auctions_by_user(user_id,startIndex,limit):
    user_auctions = auctionCollection.find({"created_by": user_id},{"bid_list":0}).sort([("_id", DESCENDING)]).skip(startIndex).limit(limit)
    return convert_to_json(setUserName_and_id(list(user_auctions), ["created_by"]))

# Function to get one auction by its ID
def get_one_auctions_by_Id(auction_id):
    auctions_data = auctionCollection.find_one({"_id": ObjectId(auction_id)},{"bid_list":0})
    uid_fld=["created_by"]
    # If the auction is not found in the main collection, check the endedAuctionCollection
    if auctions_data is None:
        auctions_data = endedAuctionCollection.find_one({"_id": ObjectId(auction_id)},{"bid_list":0})
        uid_fld.append("winner")
    return convert_to_json(setUserName_and_id(list([auctions_data]), uid_fld))

# Function to delete an auction by its ID
def delete_auction(auction_id):
    # Convert the auction_id to ObjectId type
    auction_id = ObjectId(auction_id)
    
    # Delete the auction using the delete_one method
    result = auctionCollection.delete_one({"_id": auction_id})
    
    # Check if the auction was deleted successfully
    if result.deleted_count == 1:
        return True
    else:
        return False
