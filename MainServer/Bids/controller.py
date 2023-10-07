import json
from django.http import HttpResponse, HttpResponseServerError, HttpResponseBadRequest
from django.views.decorators.csrf import csrf_exempt
from MainServer.database.Bid import get_bid_list,add_new_bid
from MainServer.verifyToken import verifyToken

@csrf_exempt
def addNewBid(request, auction_id):
    try:
        if request.method == 'POST':
            body = json.loads(request.body)
            user_id=verifyToken(request)
            bid_amount = body.get("bid_amount")
            if add_new_bid(auction_id=auction_id,user_id=user_id,bid_amount=bid_amount):
                return HttpResponse(json.dumps({"msg": "Bid added"}), content_type='application/json')
            return HttpResponse(json.dumps({"msg": "Bid not added"}), content_type='application/json')
        else:
            return HttpResponseBadRequest(json.dumps({"msg": "bad Request"}), content_type='application/json')

    except:
        return HttpResponseServerError(json.dumps({"msg": "Server Error"}), content_type='application/json')


# @csrf_exempt
# def deleteLabelController(request, u_id, labelId):
#     try:
#         if request.method == 'DELETE':
#             if deleteLabel(doc_id=u_id, labelId=labelId):
#                 return HttpResponse(json.dumps({"msg": "Lable deleted"}), content_type='application/json')
#             return HttpResponse(json.dumps({"msg": "Lable not deleted"}), content_type='application/json')
#         else:
#             return HttpResponseBadRequest(json.dumps({"msg": "bad Request"}), content_type='application/json')

#     except:
#         return HttpResponseServerError(json.dumps({"msg": "Server Error"}), content_type='application/json')


# @csrf_exempt
# def editLabelController(request, u_id, labelId):
#     try:
#         if request.method == 'POST':
#             body = json.loads(request.body)
#             newLabel = body.get("newLabel")
#             if  editLabelName(_id=u_id, labelId=labelId, newLabel=newLabel):
#                 return HttpResponse(json.dumps({"msg": "Lable edited"}), content_type='application/json')
#             return HttpResponse(json.dumps({"msg": "Lable not edited"}), content_type='application/json')
#         else:
#             return HttpResponseBadRequest(json.dumps({"msg": "bad Request"}), content_type='application/json')

#     except:
#         return HttpResponseServerError(json.dumps({"msg": "Server Error"}), content_type='application/json')


# @csrf_exempt
# def changeDefaultLabelController(request, u_id, labelId):
#     try:
#         if request.method == 'POST':
#             body = json.loads(request.body)
#             oldDefaultLableId = (body.get("oldDefaultLableId"))
#             if setDefaultLabel(_id=u_id, labelId=labelId, oldDefaultLableId=oldDefaultLableId):
#                 return HttpResponse(json.dumps({"msg": "default Lable changed"}), content_type='application/json')
#             return HttpResponse(json.dumps({"msg": "default Lable not changed"}), content_type='application/json')
#         else:
#             return HttpResponseBadRequest(json.dumps({"msg": "bad Request"}), content_type='application/json')

#     except:
#         return HttpResponseServerError(json.dumps({"msg": "Server Error"}), content_type='application/json')


def getBidListByAuctionId(request,auction_id,start,limit):
    try:
        if request.method == 'GET':
            # return HttpResponse(get_ended_auctions(startIndex,limit))
            data=get_bid_list(auction_id=auction_id,startIndex=start,limit=limit)
            return HttpResponse(data)
        else:
            return HttpResponseBadRequest(json.dumps({"msg": "bad Request"}), content_type='application/json')
    except:
        return HttpResponseServerError(json.dumps({"msg": "Server Error"}), content_type='application/json')
