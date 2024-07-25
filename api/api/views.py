from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
import pytubefix
import json
from .settings import BASE_DIR


@api_view(['GET'])
def video(request):
    video_url = request.GET.get('url', False)
    print("Video URL:",video_url)
    
    if not video_url:
        return Response({
            'status':False,
            'message':'The request must include valid youtube video url e.g. "?url=https://youtu.be/?watch=asdfdaf"'},
                        status=status.HTTP_400_BAD_REQUEST
                        )
    
    try:
        # with open(BASE_DIR/'static/VideoResponse.json','r') as f:
        #     return Response(json.load(f))
        data = pytubefix.YouTube(video_url)
        
        video_data = {
            'author':data.author,
            # 'captions':data.captions,
            # 'description':data.description,
            # 'keywords':data.keywords,
            'length':data.length,
            'thumbnail':data.thumbnail_url,
            'title':data.title,
            'views':data.views,
            # 'video_id':data.video_id,
            'publish_date':{
                'publish_year':data.publish_date.year,
                'publish_month':data.publish_date.month,
                'publish_day':data.publish_date.day,
                'publish_hour':data.publish_date.hour,
                'publish_minute':data.publish_date.minute
                },
            'streams':data.streaming_data
        }
        
        with open(BASE_DIR/'static/VideoResponse.json','w') as f:
            json.dump({'status':True,'message':'Video Found', 'video_data':video_data}, f, indent=2)
        
        return Response({'status':True,'message':'Video Found', 'video_data':video_data})
    except Exception as e:
        print(e)
        return Response({
            'status':False,
            'message':'Error occured!'})
        
    

@api_view(['GET'])
def playlist(request):
    playlist_url = request.GET.get('url', False)
    print("Playlist URL: ",playlist_url)
    
    if not playlist_url:
        return Response({
            'status':False,
            'message':'The request must include valid youtube playlist url e.g. "playlist":"https://youtu.be/?list=234dxcvc"'},
                        )
    
    try:
        with open(BASE_DIR/'static/PlaylistResponse.json','r') as f:
            res = json.load(f)
        return Response(res)
        data = pytubefix.Playlist(playlist_url)
        urls = data.video_urls
        
        videos = data.initial_data["contents"]["twoColumnBrowseResultsRenderer"]["tabs"][0]["tabRenderer"]["content"]["sectionListRenderer"]["contents"][0]["itemSectionRenderer"]["contents"][0]["playlistVideoListRenderer"]["contents"]
        videos_data = []
        for i in range(0,len(videos)):
            video = videos[i]
            videos_data.append({
                'url':urls[i],
                'video_id':video["playlistVideoRenderer"]["videoId"],
                'thumbnail':video["playlistVideoRenderer"]["thumbnail"]["thumbnails"][-1]["url"],
                'title':video["playlistVideoRenderer"]["title"]["runs"][0]["text"],
                'length':video["playlistVideoRenderer"]["lengthSeconds"],
                'views':video["playlistVideoRenderer"]["videoInfo"]["runs"][0],
                'date_ago':video["playlistVideoRenderer"]["videoInfo"]["runs"][2],
            })
        
        
        playlist_data = {
            'length':data.length,
            'owner':data.owner,
            'playlist_id':data.playlist_id,
            'title':data.title,
            'description':data.description,
            'videos':videos_data
        }
        
        res = {'status':True,'message':'Palylist Found', 'playlist_data':playlist_data}
        
        with open(BASE_DIR/'static/PlaylistResponse.json','w') as f:
            json.dump(res, f, indent=2)
        
        return Response(res)
    except Exception as e:
        print(e)
        return Response({
            'status':False,
            'message':'Error occured!'
            })