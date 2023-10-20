from django.urls import path
from MainServer.Auction.controller import *

urlpatterns = [
    # URL to add a new auction
    path('add/', AddNewAuction, name="add_auction"),
    
    # URL to Edit a auction
    path('update/<str:auction_id>', EditAuction, name="edit_auction"),
    
    # URL to delete a auction
    path('delete/<str:auction_id>', DelAuction, name="del_auction"),

    # URL to get auctions by a specific user with pagination
    path('get/byuser/<str:userId>/<int:startIndex>/<int:limit>', getAuctionsByUser, name="getAuctionsByUser"),
    
    # URL to get ended auctions with pagination
    path('get/ended/<int:startIndex>/<int:limit>', getEndedAuctions, name="get_ended_auction"),

    # URL to get upcoming auctions with pagination
    path('get/upcoming/<int:startIndex>/<int:limit>', getUpcomingAuctions, name="getUpcomingAuctions"),

    # URL to get ongoing auctions with pagination
    path('get/ongoing/<int:startIndex>/<int:limit>', getOngoingAuctions, name="getOngoingAuctions"),

    # URL to get details of a specific auction by its ID
    path('get/oneaux/<str:auction_id>', getOneAuctionById, name="getOneAuctionById"),
]
