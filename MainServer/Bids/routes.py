
from django.urls import path
from MainServer.Bids.controller import *

urlpatterns = [
    path('add/<str:auction_id>',addNewBid, name="addNewBid"),
    # path('delete/<str:u_id>/<str:labelId>', deleteLabelController, name="deleteLabel"),
    # path('edit/<str:u_id>/<str:labelId>', editLabelController, name="editLabel"),
    # path('changedefault/<str:u_id>/<str:labelId>', changeDefaultLabelController, name="changeDefaultLabel"),
    path('get/<str:auction_id>/<int:start>/<int:limit>', getBidListByAuctionId, name="getBidListByAuctionId"),
]
