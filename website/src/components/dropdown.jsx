import { useState } from 'react'


export function Dropdown({ streams, setSelectedLink }) {
    console.log("streams",streams)
    const [selected, setSelected] = useState(streams.formats[0]);
    setSelectedLink(selected.url)
    
    return (
        <>
            <div className="dropdown">
                <div className="dropdown-title">
                    <span>{selected.mimeType.split(";")[0]}</span>
                    <span>{selected.hasOwnProperty("qualityLabel") ? selected.qualityLabel : "Only Audio"}</span>
                    <span>{selected.hasOwnProperty("audioQuality") ? selected.quality : "Only Video"}</span>
                </div>
                <div className="dropdown-body">
                    {[...streams.formats, ...streams.adaptiveFormats].map((d, i) => {
                        return (
                            <div className="dropdown-option" onClick={() => {setSelected(d)}} key={i}>
                                <span>{d.mimeType.split(";")[0]}</span>
                                <span>{d.hasOwnProperty("qualityLabel") ? d.qualityLabel : "Only Audio"}</span>
                                <span>{d.hasOwnProperty("audioQuality") ? d.quality : "Only Video"}</span>
                            </div>
                        )
                    })}
                </div>
            </div>
            <a href={selected.url} className="download-target" target='_blank' rel='noreferrer' download="video"><button>Download</button></a>
        </>
    )
}