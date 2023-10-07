from datetime import datetime

AuctionSchema = {
    "start_time": datetime,
    "end_time": datetime,  
    "start_price": float,
    "item_name": str,
    "created_by": str,
    "winner": str,
    "bid_list":list,
}
BidSchema = {
    "_id":str,
    "user_id": str,
    "bid_amount": float,
    "timestamp": datetime  # Use datetime type for timestamp
}

def validate_document(document, schema):
    for field, field_type in schema.items():
        if field not in document:
            raise ValueError(f"Missing field: {field}")
        if not isinstance(document[field], field_type):
            raise ValueError(
                f"Invalid field type for {field}. Expected: {field_type.__name__}, Actual: {type(document[field]).__name__}")
