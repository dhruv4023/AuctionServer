
from django.urls import path
from MainServer.Auction.controller import *

urlpatterns = [
    path('add/', AddNewAuction, name="add_auction"),
    path('get/ended/<int:startIndex>/<int:limit>',getEndedAuctions, name="get_ended_auction"),
    path('get/upcoming/<int:startIndex>/<int:limit>',getUpcomingAuctions, name="getUpcomingAuctions"),
    path('get/ongoing/<int:startIndex>/<int:limit>',getOngoingAuctions, name="getOngoingAuctions"),
    path('get/',getAuctionsByUser, name="getAuctionsByUser"),
    path('get/oneaux/<str:auction_id>',getOneAuctionById, name="getOneAuctionById"),
]

