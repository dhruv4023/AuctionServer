
from django.conf import settings
from django.contrib import admin
from django.urls import path, include
from MainServer.home import *

urlpatterns = [
    path('', index, name="home"),
    path('api/', include('MainServer.urls')),
    path('admin/', admin.site.urls),
]
