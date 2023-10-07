import json
from jose.exceptions import ExpiredSignatureError
from django.http import HttpResponse, HttpResponseServerError, HttpResponseBadRequest,HttpResponseForbidden
from django.views.decorators.csrf import csrf_exempt
from MainServer.database.Auction import add_new_auction,get_one_auctions_by_Id,get_auctions_by_user,get_ongoing_auctions,delete_auction,get_upcoming_auctions
from MainServer.database.EndedAuction import get_ended_auctions
from MainServer.OtherFun import anyDateTimeTo_datetime_Formate
from MainServer.verifyToken import verifyToken

@csrf_exempt
def AddNewAuction(request):
    try:
        if request.method == 'POST':
            body = json.loads(request.body)
            user_id=verifyToken(request)
            item_name=body.get("item_name")
            start_price=body.get("start_price")
            # print(start_price)
            end_time= anyDateTimeTo_datetime_Formate(body.get("end_time"),"%Y-%m-%d %H:%M")
            start_time= anyDateTimeTo_datetime_Formate(body.get("start_time"),"%Y-%m-%d %H:%M")
            if add_new_auction(user_id=user_id,item_name=item_name,start_price=start_price,end_time=end_time,start_time=start_time):
                return HttpResponse(json.dumps({"msg": "Auction Started"}), content_type='application/json')
            return HttpResponse(json.dumps({"msg": "Auction Not Started"}), content_type='application/json')
        else:
            return HttpResponseBadRequest(json.dumps({"msg": "bad Request"}), content_type='application/json')

    except:
        return HttpResponseServerError(json.dumps({"msg": "Server Error"}), content_type='application/json')


@csrf_exempt
def getEndedAuctions(request,startIndex,limit):
    # try:
        if request.method == 'GET':
            # return HttpResponse(get_ended_auctions(startIndex,limit))
            data=get_ended_auctions(startIndex,limit)
            return HttpResponse(data)
        else:
            return HttpResponseBadRequest(json.dumps({"msg": "bad Request"}), content_type='application/json')
    # except:
    #     return HttpResponseServerError(json.dumps({"msg": "Server Error"}), content_type='application/json')

@csrf_exempt
def getOngoingAuctions(request,startIndex,limit):
    try:
        if request.method == 'GET':
            # return HttpResponse(get_ended_auctions(startIndex,limit))
            data=get_ongoing_auctions(startIndex,limit)
            return HttpResponse(data)
        else:
            return HttpResponseBadRequest(json.dumps({"msg": "bad Request"}), content_type='application/json')
    except:
        return HttpResponseServerError(json.dumps({"msg": "Server Error"}), content_type='application/json')

@csrf_exempt
def getUpcomingAuctions(request,startIndex,limit):
    try:
        if request.method == 'GET':
            # return HttpResponse(get_ended_auctions(startIndex,limit))
            data=get_upcoming_auctions(startIndex,limit)
            return HttpResponse(data)
        else:
            return HttpResponseBadRequest(json.dumps({"msg": "bad Request"}), content_type='application/json')
    except:
        return HttpResponseServerError(json.dumps({"msg": "Server Error"}), content_type='application/json')

@csrf_exempt
def getAuctionsByUser(request):
    try:
        user_id=verifyToken(request)
        if request.method == 'GET':
            # return HttpResponse(get_ended_auctions(startIndex,limit))
            data=get_auctions_by_user(user_id)
            return HttpResponse(data)
        else:
            return HttpResponseBadRequest(json.dumps({"msg": "bad Request"}), content_type='application/json')
    
    except:
        return HttpResponseServerError(json.dumps({"msg": "Server Error"}), content_type='application/json')


def getOneAuctionById(request,auction_id):
    try:
        if request.method == 'GET':
            # return HttpResponse(get_ended_auctions(startIndex,limit))
            data=get_one_auctions_by_Id(auction_id)
            return HttpResponse(data)
        else:
            return HttpResponseBadRequest(json.dumps({"msg": "bad Request"}), content_type='application/json')
    except:
        return HttpResponseServerError(json.dumps({"msg": "Server Error"}), content_type='application/json')
