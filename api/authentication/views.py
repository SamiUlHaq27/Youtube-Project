from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.http.request import HttpRequest
from rest_framework import status
import datetime
import json
import jwt

encoder = 'my_secret_31241'
time_format = '%d%m%Y%H%M%S'

@api_view(['POST'])
def authorize(request:HttpRequest):
    body = json.loads(request.body.decode('utf-8'))
    username:str = body.get("username", None)
    password:str = body.get("password", None)
    
    
    if(not username):
        return Response({
            'message':'username is not present in request',
            
            }, status=status.HTTP_405_METHOD_NOT_ALLOWED)
        
    if(not password):
        return Response({
            'message':'password is not present in request',
            
            }, status=status.HTTP_405_METHOD_NOT_ALLOWED)
        
    user = authenticate(username=username, password=password)
    
    if(not user):
        return Response({
            'message':'incorrect name or password',
            
            }, status=status.HTTP_401_UNAUTHORIZED)
        
    return Response({
        'message':'authentication successfull',
        'token':jwt.encode({
            "id":user.id,
            "un":user.username,
            "cat":datetime.datetime.now().strftime(time_format)
            }, encoder, algorithm='HS256')
    }, status=status.HTTP_202_ACCEPTED)

def verify(token):
        
    try:
        data = jwt.decode(token, encoder, algorithms=["HS256"])
    except Exception as e:
        raise Exception("Error occured")
    
    time_passed = datetime.datetime.now() - datetime.datetime.strptime(data['cat'], time_format)
    
    if(time_passed.seconds > 1800):
        raise TimeoutError("Token expired")
    
    return data
