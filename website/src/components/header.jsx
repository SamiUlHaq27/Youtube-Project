import logo from '../images/logo.png'

export function Header(){
    return(
        <div className="header">
            <div className="logo-div">
                <img src={logo} alt="" srcset="" />
            </div>
            <div className="pages-div">
                <ul>
                    <a href="#"><li>Home</li></a>
                    <a href="#"><li>Terms Of Use</li></a>
                    <a href="#"><li>Privacy Policy</li></a>
                    <a href="#"><li>About Us</li></a>
                </ul>
            </div>
        </div>
    )
}