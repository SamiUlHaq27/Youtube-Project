import logo from '../images/logo.png'


export function Footer(){
    return(
        <div className="footer header">
            <div className="logo-div">
                <img src={logo} alt="" srcset="" />
            </div>
            <div className="copyright-div">
                <h3>Copyright YTPD, 2024</h3>
            </div>
        </div>
    )
}