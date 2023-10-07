from django.urls import path, include
from MainServer.home import *

urlpatterns = [
    path('auction/', include('MainServer.Auction.routes')),
    path('bids/', include('MainServer.Bids.routes')),
]
