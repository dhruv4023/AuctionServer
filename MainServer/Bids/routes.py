from django.urls import path
from MainServer.Bids.controller import *

urlpatterns = [
    # URL pattern to add a new bid for a specific auction
    path('add/<str:auction_id>', addNewBid, name="addNewBid"),

    # URL pattern to get the bid list for a specific auction with pagination
    path('get/<str:auction_id>/<int:start>/<int:limit>', getBidListByAuctionId, name="getBidListByAuctionId"),
]
