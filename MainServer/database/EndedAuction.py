from  MainServer.database.db import *
from  MainServer.database.Users import setUserName_and_id
from  MainServer.database.Auction import delete_auction


# to retrive transactions
def get_ended_auctions(startIndex: int = 0, limit: int = 10):
    return convert_to_json(setUserName_and_id(list(endedAuctionCollection.find({},{"bid_list":0}).sort([("_id", DESCENDING)]).skip(startIndex).limit(limit)),["created_by","winner"]))

def set_winner_for_ended_auctions():
    current_time = datetime.now()
    ended_auctions= auctionCollection.find({"end_time": {"$lt": current_time}})
    for aux in ended_auctions:
        aux["winner"]=aux["bid_list"][0]["user_id"]
        # print(aux)
        try:
            id=aux["_id"]
            del aux["_id"]
            print(endedAuctionCollection.insert_one(aux).inserted_id)
            delete_auction(id)
        except:
            print("error")
            pass