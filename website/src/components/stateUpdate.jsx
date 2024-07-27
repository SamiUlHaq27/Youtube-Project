import { useState } from "react";

export function StateUpdate() {
    
    var [numbers, setNumbers] = useState([0])

    function run(i) {
        for (let i = 1; i < 10; i++) {
            setNumbers((numbers)=>{
                return([...numbers,i])
            })
            
        }
    }

    function reset() {
        setNumbers([0])
    }

    return(
        <>
        <h4>{numbers}</h4>
        <button onClick={reset}>reset</button>
        <button onClick={()=>{run(0)}}>run</button>
        </>
    );
}