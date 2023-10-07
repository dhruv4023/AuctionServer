from  MainServer.database.db import *
from MainServer.database.Users import setUserName_and_id

# Function to add a new bid to the bid_list array
def add_new_bid(auction_id: str, user_id: str, bid_amount: float):
    # Create a document with bid details
    doc = {
        "_id": str(getUniqueId()),
        "user_id": user_id,
        "bid_amount": float(bid_amount),
        "timestamp": datetime.now(),
    }
    
    # Validate the bid document using a schema (BidSchema)
    validate_document(document=doc, schema=BidSchema)
    
    # Define the query and update operation to add the bid to the auction
    query = {"_id": ObjectId(auction_id)}
    update = {
        "$push": {"bid_list": {"$each": [doc], "$position": 0}},
    }
    
    # Perform the update operation and return the result
    return updateOne(query, update)

# Function to delete a bid from the bid_list array
def delete_bid(auction_id: str, bid_id: str):
    # Define the query and update operation to remove the bid from the auction
    query = {"_id": ObjectId(auction_id)}
    update = {
        "$pull": {
            "bid_list": {
                "_id": bid_id,
            }
        }
    }
    
    # Perform the update operation and return the result
    return updateOne(query, update)

# Function to retrieve the bid_list
def get_bid_list(auction_id: str, startIndex: int = 0, limit: int = 10):
    # Define the query to retrieve the bid_list from the auction
    query = {"_id": ObjectId(auction_id)}
    
    # Retrieve the bid_list with pagination using the $slice operator
    bid_lst = auctionCollection.find_one(
        query,
        {"bid_list": {"$slice": [startIndex, limit]}, "start_time": 0, "end_time": 0, "start_price": 0, "item_name": 0, "created_by": 0}
    )
    
    # Convert and return the bid_list as JSON
    return convert_to_json(setUserName_and_id(list(bid_lst["bid_list"]), ["user_id"]))

# Common function to update a document
def updateOne(query, update):
    return auctionCollection.update_one(query, update).modified_count
