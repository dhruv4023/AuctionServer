from MainServer.database.db import  AUTH_SERVER_API
from MainServer.database.CustomError import   APIDataFetchError
import requests 
# Function to replace user IDs with user names in a list of dictionaries
def setUserName_and_id(data: list, u_id_fields: list):
    modified_data = []  # Create an empty list to store modified dictionaries
    # Iterate through each dictionary in the 'data' list
    users={}
    for item in data:
        # Iterate through the specified fields to process
        for field in u_id_fields:
            user_id = item.get(field)  # Get the user ID from the dictionary field

            # Retrieve user data based on the user ID from the 'users' collection
            user_data=users.get(user_id)
            if user_data is None and user_id is not None:
                print("db")
                user_data =  getUserData(user_id)
                users[user_id]=user_data
            else:    
                print("cache used")
            # print(user_data)
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


def getUserData(userId):
    # Define the URL of the API you want to fetch data from
            # Make an HTTP GET request to the API        
    response =  requests.get(f"{AUTH_SERVER_API}/user/get/{userId}")

    # Check if the request was successful (status code 200)
    if response.status_code == 200:
        # Parse the JSON response from the API
        data = response.json()
        return (data)  # Return the data as JSON response
    else:
        # Handle errors or return an appropriate response
        raise APIDataFetchError("Failed to retrieve data from the API")
            
