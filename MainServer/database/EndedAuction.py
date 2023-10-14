from  MainServer.database.db import *
from  MainServer.database.Users import setUserName_and_id
from  MainServer.database.Auction import delete_auction

# Retrieve ended auctions from the database
def get_ended_auctions(startIndex: int = 0, limit: int = 10):
    return convert_to_json(setUserName_and_id(list(endedAuctionCollection.find({}, {"bid_list": 0})
        .sort([("_id", DESCENDING)]).skip(startIndex).limit(limit)), ["created_by", "winner"]))

# Set the winner for ended auctions based on the highest bid
def set_winner_for_ended_auctions():
    current_time = datetime.now()
    
    # Find auctions whose end_time is less than the current time
    ended_auctions = auctionCollection.find({"end_time": {"$lt": current_time}})
    
    for aux in ended_auctions:
        try:
            aux["winner"] = aux["bid_list"][0]["user_id"]
        except:
            aux["winner"]= None
        try:
            id = aux["_id"]
            del aux["_id"]
            
            # Insert the auction into the endedAuctionCollection and delete it from the auctionCollection
            print(endedAuctionCollection.insert_one(aux).inserted_id)
            delete_auction(id)
        except:
            print("error")
            pass
