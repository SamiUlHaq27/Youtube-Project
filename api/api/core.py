from .settings import BASE_DIR
import pytubefix
import json

raw = True

def getVideo(video_url):
    
    #----------------------------------- Raw Data ------------------------------------
    if raw:
        with open(BASE_DIR/'static/VideoResponse.json','r') as f:
            return json.load(f)
            
    #----------------------------------- Actual Data ----------------------------------
    data = pytubefix.YouTube(video_url)
    
    video_data = {
        'author':data.author,
        'length':data.length,
        'thumbnail':data.thumbnail_url,
        'title':data.title,
        'views':data.views,
        'publish_date':{
            'publish_year':data.publish_date.year,
            'publish_month':data.publish_date.month,
            'publish_day':data.publish_date.day,
            'publish_hour':data.publish_date.hour,
            'publish_minute':data.publish_date.minute
            },
        'streams':data.streaming_data
    }
    
    #----------------------------------- Saving Data -----------------------------------
    with open(BASE_DIR/'static/VideoResponse.json','w') as f:
        json.dump(video_data, f, indent=2)
    
    return video_data
    
def getPlaylist(playlist_url):
    
    #----------------------------------- Raw Data ------------------------------------
    if raw:
        with open(BASE_DIR/'static/PlaylistResponse.json','r') as f:
            return json.load(f)
    
    #----------------------------------- Actual Data ----------------------------------
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
        'videos':videos_data
    }
    
    #----------------------------------- Saving Data -----------------------------------
    with open(BASE_DIR/'static/PlaylistResponse.json','w') as f:
        json.dump(playlist_data, f, indent=2)
    
    return playlist_data