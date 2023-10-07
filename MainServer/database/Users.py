
from MainServer.database. db import users,ObjectId
 

def setUserName_and_id(data:list,u_id_fields:list):
    modified_auctions = []    
    # print(u_id_fields)
    for auction in data:
        for fld in u_id_fields:
            # print(fld)
            user_id = auction.get(fld)   
                     
            # Retrieve the user's name from the users collection based on user_id
            # print(len(user_id))
            user_data = users.find_one({"_id":ObjectId( user_id)})
            
            # Replace created_id with the user's name in the auction document
            doc={
                "_id":auction[fld] ,
                "name": user_data["firstName"]+" "+user_data["lastName"] if user_data else "Unknown"
            }
            auction[fld] = doc
        modified_auctions.append(auction)
    return modified_auctions

