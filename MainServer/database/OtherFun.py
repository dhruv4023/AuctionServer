import time

from bson import ObjectId
from datetime import datetime


def custom_serializer(obj):
    if isinstance(obj, ObjectId):
        return str(obj)
    if isinstance(obj, datetime):
        return obj.isoformat()  # Convert datetime to ISO 8601 format
    raise TypeError(f"Object of type {type(obj)} is not JSON serializable")

import json
def convert_to_json(data):
    return json.dumps(data, default=custom_serializer, indent=4)

def getUniqueId():
    return int(time.time()*10000)

