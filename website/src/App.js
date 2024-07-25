import "./App.css";
import "./css/style.css";
import { useState } from "react";
import { Header } from "./components/header";
import { Footer } from "./components/footer";
import { SearchBar } from "./components/searchBar";
import { Video } from "./components/video";
import { Playlist } from "./components/playlist";

function App() {
  var endpoint = "http://127.0.0.1:8000/";

  var [videosData, setVideosData] = useState([]);
  var [playlistsData, setPlaylistsData] = useState([]);

  function removeVideoData(index) {
    let list = [];
    for (let i = 0; i < videosData.length; i++) {
      if (i !== index) {
        list.push(videosData[i]);
      }
    }
    setVideosData(list);
  }

  function getUrl(searchUrl) {
    if (searchUrl.includes("playlist")) {
      getPlaylist(searchUrl);
    } else if (searchUrl.includes("youtu")) {
      getVideo(searchUrl);
    } else {}
  }

  function getVideo(url) {
    fetch(endpoint + "video/?url=" + url)
      .then((response) => response.json())
      .then((data) => {
        if (data.status) {
          console.log("updating data")
          data.type = "video";
          setVideosData([...videosData, data]);
        }
      })
      .catch((error) => {
        console.error("Error: ", error);
      });
  }

  function getPlaylist(url) {
    fetch(endpoint+"playlist/?url="+url)
    .then((response)=>response.json())
    .then((data)=>{
      console.log(data)
      if (data.status) {
        data.type = "playlist"
        setPlaylistsData([...playlistsData,data])
      }
    })
  }

  function getAllPlaylistVideos(urls){
    for (let index = 0; index < urls.length; index++) {
      getVideo(urls[index])
    }
  }

  return (
    <>
      <Header />
      <div className="main-title">
        <h1>Youtube Video & Playlist Downlaoder</h1>
        <p>
          Paste the link of youtube video or playlist below and click the
          dowload icon
        </p>
      </div>
      <SearchBar getter={getUrl} />
      {videosData.length ? (
        <>
          <div className="videos-display">
            {videosData
              .filter((data, i) => {
                return data.type === "video";
              })
              .map((v, i) => {
                return(<Video data={v} remover={removeVideoData} index={i} key={i} />)
              })}
          </div>
          <div className="videos-buttons">
            <button>Download All</button>
          </div>
        </>
      ) : (
        <></>
      )}
      {playlistsData.length?(<>
        {playlistsData
              .filter((data, i) => {
                return data.type === "playlist";
              })
              .map((p, i) => {
                  return(<Playlist data={p} getVideo={getUrl} getAllVideos={getAllPlaylistVideos} key={i} />)
              })}
      </>):(<></>)}
      <Footer />
    </>
  );
}

export default App;
