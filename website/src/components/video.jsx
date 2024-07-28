import { Dropdown } from "./dropdown"


export function Video({data, remover, index, selected}){
    console.log("video",data)
    function getLength(seconds) {
        let hours = Math.floor(seconds/3600)
        seconds = seconds%3600
        let mins = Math.floor(seconds/60)
        seconds = seconds%60
        return(hours+":"+mins+":"+seconds)
    }

    function setSelectedLink(link) {
        selected[index] = link
        console.log("Selected Links: ",selected)
    }

    return(
        <div className="video">
            <div className="cross-icon" onClick={()=>{remover(index)}}>
                <h2>X</h2>
            </div>
            <div className="thumbnail">
                <img src={data.video_data.thumbnail} alt="" />
            </div>
            <div className="video-details">
                <h3 className="video-title">{data.video_data.title}</h3>
                <h4 className="video-property">Author: {data.video_data.author} | </h4>
                <h4 className="video-property">Length: {getLength(data.video_data.length)} | </h4>
                <h4 className="video-property">Views: {data.video_data.views}</h4>
                <div className="video-download">
                    <Dropdown streams={data.video_data.streams} setSelectedLink={setSelectedLink}/>
                </div>
            </div>
        </div>
    )
}