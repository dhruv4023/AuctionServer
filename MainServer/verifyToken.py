import os
import json
from jose import jwt,ExpiredSignatureError
from dotenv import load_dotenv
from django.http import  HttpResponseForbidden
# Load environment variables from .env file
load_dotenv()
def verifyToken(request):
    try:
        token = request.META.get('HTTP_AUTHORIZATION')
        payload=jwt.decode(token[7:],os.getenv("JWT_SECRECT"))
        return payload["userId"]
        
    except ExpiredSignatureError:
        return HttpResponseForbidden(json.dumps({'msg': 'Access token has expired'}), content_type='application/json')
    