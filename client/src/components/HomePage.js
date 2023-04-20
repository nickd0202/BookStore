import React from "react";
import "../CSS/Home.css";

function HomePage(){

    

    return (
        // <div style={{ backgroundImage:`url(https://www.canva.com/design/DAFgmg0nmkQ/yD-iAZHHIRNw3GuY9MBFNA/edit?utm_content=DAFgmg0nmkQ&utm_campaign=designshare&utm_medium=link2&utm_source=sharebutton)` }}>
            
        // </div>
        <div class="homebg">
            <video className='videoTag' autoPlay loop muted>
                <source src={"https://cdn.discordapp.com/attachments/1079947255399862334/1098435365561454612/Get_started_in_Canva_1.mp4"} type='video/mp4' />
            </video>
        </div>
    )
}
export default HomePage;