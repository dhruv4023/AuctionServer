import json
from django.http import HttpResponse, HttpResponseServerError, HttpResponseBadRequest
from django.views.decorators.csrf import csrf_exempt
from MainServer.database.Bid import get_bid_list, add_new_bid
from MainServer.verifyToken import verifyToken

@csrf_exempt
def addNewBid(request, auction_id):
    try:
        if request.method == 'POST':
            # Parse JSON request body
            body = json.loads(request.body)
            user_id = verifyToken(request)
            bid_amount = body.get("bid_amount")

            # Call the function to add a new bid
            if add_new_bid(auction_id=auction_id, user_id=user_id, bid_amount=bid_amount):
                return HttpResponse(json.dumps({"msg": "Bid added"}), content_type='application/json')
            return HttpResponse(json.dumps({"msg": "Bid not added"}), content_type='application/json')
        else:
            return HttpResponseBadRequest(json.dumps({"msg": "Bad Request"}), content_type='application/json')
    except:
        return HttpResponseServerError(json.dumps({"msg": "Server Error"}), content_type='application/json')

def getBidListByAuctionId(request, auction_id, start, limit):
    try:
        if request.method == 'GET':
            # Call the function to get the bid list for a specific auction with pagination
            data = get_bid_list(auction_id=auction_id, startIndex=start, limit=limit)
            return HttpResponse(data)
        else:
            return HttpResponseBadRequest(json.dumps({"msg": "Bad Request"}), content_type='application/json')
    except:
        return HttpResponseServerError(json.dumps({"msg": "Server Error"}), content_type='application/json')
