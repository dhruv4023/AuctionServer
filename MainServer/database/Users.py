from MainServer.database.db import users, ObjectId

# Function to replace user IDs with user names in a list of dictionaries
def setUserName_and_id(data: list, u_id_fields: list):
    modified_data = []  # Create an empty list to store modified dictionaries
    
    # Iterate through each dictionary in the 'data' list
    for item in data:
        # Iterate through the specified fields to process
        for field in u_id_fields:
            user_id = item.get(field)  # Get the user ID from the dictionary field

            # Retrieve user data based on the user ID from the 'users' collection
            user_data = users.find_one({"_id": ObjectId(user_id)})

            # Create a new dictionary with the user's name and user ID
            user_info = {
                "_id": user_id,
                "name": user_data["firstName"] + " " + user_data["lastName"] if user_data else "Unknown"
            }

            # Replace the original field in the dictionary with user_info
            item[field] = user_info

        # Append the modified dictionary to the 'modified_data' list
        modified_data.append(item)

    # Return the list of dictionaries with user names instead of user IDs
    return modified_data
