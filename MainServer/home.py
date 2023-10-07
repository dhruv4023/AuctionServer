from django.shortcuts import render
from django.http import *
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def index(request):
    return HttpResponse("Server is running")