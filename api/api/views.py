from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.http.request import HttpRequest
from rest_framework import status
from .core import getPlaylist, getVideo
from authentication.views import verify


@api_view(['GET'])
def video(request:HttpRequest):
    print('Path',request.path)
    print(request.GET)
    token = request.GET.get('token',False)
    
    if(not token):
        return Response({
            'status':False,
            'message':'Authorization credentials were not provided'
            }, status=status.HTTP_401_UNAUTHORIZED)

    try:
        data = verify(token)
    except TimeoutError as e:
        return Response({
            'status':False,
            'message':"Token expired"
            }, status=status.HTTP_401_UNAUTHORIZED)
    except Exception as e:
        return Response({
            'status':False,
            'message':"Error occured"
            }, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    
    # ---------------------------- Processing Request -----------------------------------------
    video_url = request.GET.get('url', False)
    print("Video URL:",video_url)
    if not video_url:
        return Response({
            'status':False,
            'message':'The request must include valid youtube video url e.g. "?url=https://youtu.be/?watch=asdfdaf"'
            }, status=status.HTTP_405_METHOD_NOT_ALLOWED)
    
    try:
        video_data = getVideo(video_url)
        return Response({
            'status':True,
            'message':'Video Found',
            'video_data':video_data
            }, status=status.HTTP_200_OK)
    except Exception as e:
        print(e)
        return Response({
            'status':False,
            'message':'Error occured!'
            }, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        
@api_view(['GET'])
def playlist(request):
    
    token = request.GET.get('token',False)
    
    if(not token):
        return Response({
            'status':False,
            'message':'Authorization credentials were not provided'
            }, status=status.HTTP_401_UNAUTHORIZED)

    try:
        data = verify(token)
    except TimeoutError as e:
        return Response({
            'status':False,
            'message':"Token expired"
            }, status=status.HTTP_401_UNAUTHORIZED)
    except Exception as e:
        return Response({
            'status':False,
            'message':"Error occured"
            }, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    
    # ---------------------------- Processing Request -----------------------------------------
    playlist_url = request.GET.get('url', False)
    print("Playlist URL: ",playlist_url)
    if not playlist_url:
        return Response({
            'status':False,
            'message':'The request must include valid youtube playlist url e.g. "playlist":"https://youtu.be/?list=234dxcvc"'},
                        )
    
    try:
        playlist_data = getPlaylist(playlist_url)
        return Response({
            'status':True,
            'message':'Palylist Found', 'playlist_data':playlist_data
            }, status=status.HTTP_200_OK)
    except Exception as e:
        print(e)
        return Response({
            'status':False,
            'message':'Error occured!'
            }, status=status.HTTP_500_INTERNAL_SERVER_ERROR)