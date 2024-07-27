import { useEffect, useState } from "react";
import LoadIcon from '../images/loading.gif'
import DownIcon from "../images/download.png";


export function SearchBar({ getter, videos , playlists }) {

  const [url, setUrl] = useState("");
  var [icon, setIcon] = useState(DownIcon)
  
  useEffect(()=>{
    setIcon(()=>{
      return(DownIcon)
    })
  },[videos,playlists])

  function getData() {
    if (icon === DownIcon) {
      setIcon(LoadIcon)
      getter(url)
    }
  }

  return (
    <div className="search-bar">
      <div className="inner-search-bar">
        <input
          type="text"
          placeholder="Paste Link Here..."
          id="search-input"
          value={url}
          onChange={(event) => setUrl(event.target.value)}
          onKeyDown={(event)=>{
            if (event.key === 'Enter') {
              getData()
            }
          }}
        />
        <div className="icon-wrap" onClick={()=>getData()}>
          <img src={icon} alt="loading" srcset="" />
        </div>
      </div>
    </div>
  );
}
