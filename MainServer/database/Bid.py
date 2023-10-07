from  MainServer.database.db import *
from MainServer.database.Users import setUserName_and_id



# to add new transaction to bid_list array
def add_new_bid(auction_id:str,user_id:str,bid_amount:float):
    doc = {
        "_id":str(getUniqueId()),
        "user_id": user_id,
        "bid_amount": float(bid_amount),
        "timestamp": datetime.now(),
    }
    validate_document(document=doc, schema=BidSchema)
    query = {"_id": ObjectId(auction_id)}
    update = {
        "$push": {"bid_list": {"$each": [doc], "$position": 0}},
    }
    return updateOne(query,update)


# to delete a transaction from bid_list array
def delete_bid(auction_id: str, bid_id:str):
    query = {"_id": ObjectId(auction_id)}
    update = {
        "$pull": {
            "bid_list": {
                "_id":bid_id,
            }
        }
    }
    return updateOne(query, update)

# to retrive bid_list
def get_bid_list(auction_id: str, startIndex: int = 0, limit: int = 10):
    query = {"_id": ObjectId(auction_id)}
    bid_lst=auctionCollection.find_one(query, {"bid_list": {"$slice": [startIndex, limit]}, "start_time":0,"end_time":0,"start_price":0,"item_name":0,"created_by":0})
    return convert_to_json(setUserName_and_id(list(bid_lst["bid_list"]),["user_id"]))

# common updateOne function
def updateOne(query, update):
    return auctionCollection.update_one(query, update).modified_count
