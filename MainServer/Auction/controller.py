import json
from jose.exceptions import ExpiredSignatureError
from django.http import HttpResponse, HttpResponseServerError, HttpResponseBadRequest, HttpResponseForbidden
from django.views.decorators.csrf import csrf_exempt
from MainServer.database.Auction import add_new_auction,edit_auction,get_one_auctions_by_Id,get_auctions_by_user,get_ongoing_auctions,delete_auction,get_upcoming_auctions
from MainServer.database.EndedAuction import get_ended_auctions
from MainServer.OtherFun import anyDateTimeTo_datetime_Formate
from MainServer.verifyToken import verifyToken

# Define a view to add a new auction
@csrf_exempt
def AddNewAuction(request):
    try:
        if request.method == 'POST':
            
            body = json.loads(request.body)
            user_id = verifyToken(request)
            item_name = body.get("item_name")
            start_price = body.get("start_price")
            end_time = anyDateTimeTo_datetime_Formate(body.get("end_time"), "%Y-%m-%d %H:%M")
            start_time = anyDateTimeTo_datetime_Formate(body.get("start_time"), "%Y-%m-%d %H:%M")
            
            # Attempt to add a new auction
            if add_new_auction(user_id=user_id, item_name=item_name, start_price=start_price, end_time=end_time, start_time=start_time):
                return HttpResponse(json.dumps({"msg": "Auction Started"}), content_type='application/json')
            return HttpResponse(json.dumps({"msg": "Auction Not Started"}), content_type='application/json')
        else:
            return HttpResponseBadRequest(json.dumps({"msg": "bad Request"}), content_type='application/json')

    except:
        return HttpResponseServerError(json.dumps({"msg": "Server Error"}), content_type='application/json')

@csrf_exempt
def EditAuction(request,auction_id):
    # print(request.method,auction_id)
    try:
        if request.method == 'PUT':
            body = json.loads(request.body)
            user_id = verifyToken(request)
            item_name = body.get("item_name")
            start_price = body.get("start_price")
            end_time = anyDateTimeTo_datetime_Formate(body.get("end_time"), "%Y-%m-%d %H:%M")
            start_time = anyDateTimeTo_datetime_Formate(body.get("start_time"), "%Y-%m-%d %H:%M")
            
            # Attempt to add a new auction
            if edit_auction(auction_id=auction_id,user_id=user_id, item_name=item_name, start_price=start_price, end_time=end_time, start_time=start_time):
                return HttpResponse(json.dumps({"msg": "Auction Started"}), content_type='application/json')
            return HttpResponse(json.dumps({"msg": "Auction Not Started"}), content_type='application/json')
        else:
            return HttpResponseBadRequest(json.dumps({"msg": "bad Request"}), content_type='application/json')

    except:
        return HttpResponseServerError(json.dumps({"msg": "Server Error"}), content_type='application/json')

# Define a view to get ended auctions
@csrf_exempt
def getEndedAuctions(request,startIndex,limit):
    # try:
        if request.method == 'GET':
            # return HttpResponse(get_ended_auctions(startIndex,limit))
            # print(startIndex)
            data=get_ended_auctions(startIndex,limit)
            return HttpResponse(data)
        else:
            return HttpResponseBadRequest(json.dumps({"msg": "bad Request"}), content_type='application/json')
    # except:
    #     return HttpResponseServerError(json.dumps({"msg": "Server Error"}), content_type='application/json')

# Define a view to get ongoing auctions
@csrf_exempt
def getOngoingAuctions(request,startIndex,limit):
    try:
        if request.method == 'GET':
            data = get_ongoing_auctions(startIndex,limit)
            return HttpResponse(data)
        else:
            return HttpResponseBadRequest(json.dumps({"msg": "bad Request"}), content_type='application/json')
    except:
        return HttpResponseServerError(json.dumps({"msg": "Server Error"}), content_type='application/json')

# Define a view to get upcoming auctions
@csrf_exempt
def getUpcomingAuctions(request,startIndex,limit):
    try:
        if request.method == 'GET':
            data = get_upcoming_auctions(startIndex,limit)
            return HttpResponse(data)
        else:
            return HttpResponseBadRequest(json.dumps({"msg": "bad Request"}), content_type='application/json')
    except:
        return HttpResponseServerError(json.dumps({"msg": "Server Error"}), content_type='application/json')

# Define a view to get auctions by user
@csrf_exempt
def getAuctionsByUser(request,userId,startIndex,limit):
    try:
        # user_id = verifyToken(request)
        if request.method == 'GET':
            data = get_auctions_by_user(userId,startIndex,limit)
            return HttpResponse(data)
        else:
            return HttpResponseBadRequest(json.dumps({"msg": "bad Request"}), content_type='application/json')
    except:
        return HttpResponseServerError(json.dumps({"msg": "Server Error"}), content_type='application/json')

# Define a view to get one auction by its ID
def getOneAuctionById(request,auction_id):
    try:
        if request.method == 'GET':
            data = get_one_auctions_by_Id(auction_id)
            return HttpResponse(data)
        else:
            return HttpResponseBadRequest(json.dumps({"msg": "bad Request"}), content_type='application/json')
    except:
        return HttpResponseServerError(json.dumps({"msg": "Server Error"}), content_type='application/json')

# Define a view to get one auction by its ID
@csrf_exempt
def DelAuction(request,auction_id):
    # try:
        user_id = verifyToken(request)
        # print(user_id)
        if request.method == 'DELETE':
            if  delete_auction(auction_id,user_id):
                return HttpResponse(json.dumps({"msg": "Delete Successfully"}), content_type='application/json')
            return HttpResponse(json.dumps({"msg": "Failed to Delete"}), content_type='application/json')
        else:
            return HttpResponseBadRequest(json.dumps({"msg": "bad Request"}), content_type='application/json')
    # except:
    #     return HttpResponseServerError(json.dumps({"msg": "Server Error"}), content_type='application/json')
