export function Playlist({data, getVideo, getAllVideos}) {

  function getAll() {
    let urls = []
    for (let index = 0; index < data.playlist_data.videos.length; index++) {
      urls.push(data.playlist_data.videos[index].url)
    }
    getAllVideos(urls);
  }

  // function getAll() {
  //   for (let index = 0; index < data.playlist_data.videos.length; index++) {
  //     getVideo(data.playlist_data.videos[index].url)
  //   }
  // }

  function getLength(seconds) {
    let hours = Math.floor(seconds/3600)
    seconds = seconds%3600
    let mins = Math.floor(seconds/60)
    seconds = seconds%60
    return(hours+":"+mins+":"+seconds)
}

  return (
    <div className="playlist">
      <div className="playlist-head">
        <div className="playlist-details">
            <h3>Total: {data.playlist_data.length}</h3>
            <h2 className="default-title">{data.playlist_data.title}</h2>
            <h3>{data.playlist_data.owner}</h3>
        </div>
        <div className="playlist-head-thumbnail">
          <img src={data.playlist_data.thumbnail} alt="" />
        </div>
        <div className="playlist-buttons">
          <button onClick={getAll}>Get All</button>
        </div>
      </div>
      <div className="playlist-videos">
        {data.playlist_data.videos.map((video,i)=>{
          return(
            <div className="playlist-video" key={i}>
                <h1 className="video-number">{i+1} </h1>
              <div className="playlist-thumbnail">
                <img src={video.thumbnail} alt="" />
              </div>
              <div className="playlist-video-details">
                <h2>{video.title}</h2>
                <span>{getLength(video.length)}</span>
                <span>{video.views.text}</span>
                <span>{video.date_ago.text}</span>
                <button onClick={()=>getVideo(video.url)}>Get</button>
              </div>
            </div>
          )
        })}
      </div>
    </div>
  );
}
