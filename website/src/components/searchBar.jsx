import { useState } from 'react'
import Icon from '../images/download.png'


export function SearchBar({getter}) {

    const [url, setUrl] = useState("")

    return(
        <div className="search-bar">
            <div className="inner-search-bar">
                <input type="text" placeholder="Paste Link Here..." value={url} onChange={(event)=>(setUrl(event.target.value))}/>
                <div className="icon-wrap" onClick={()=>getter(url)}>
                    <img src={Icon} alt="" srcset="" />
                </div>
            </div>
        </div>
    )
}