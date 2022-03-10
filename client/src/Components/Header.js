import React, { Component } from "react";
import { Helmet } from "react-helmet";
import { Link , Redirect} from "react-router-dom";

class Header extends React.Component {
  constructor(props) {
    super(props);

   this.state = {

      login: false
      
    }
    
    this.logout = this.logout.bind(this);
  
  }
componentDidMount() {
    if (localStorage.getItem('login')) {
      
       this.setState({login:false})
     
      }
      else{
        this.setState({login:true})
      }
  }

logout(){
    localStorage.setItem("login",'');
    localStorage.clear();
    localStorage.setItem('login', JSON.stringify({
      login:false,
      store:null
   
  }))
    this.setState({login: true});
  }
  render() {
    console.warn(this.state.login);
    return (
      <div>
        <header className="header-section">
          <div className="container">
            <ul className="main-menu-left site-menu-style">
              <li>
                <Link to="/">Home</Link>
              </li>
              <li>
                <Link to="/wishlist">My Wishlist </Link>
              </li>
              <li>
                <Link to="category">Events</Link>
              </li>
            </ul>
            <Link to="/">
              {" "}
              <a className="site-logo">
                <img style = {{width:'80px'}} src="img/logo.png" alt="" />
              </a>{" "}
            </Link>
            <ul className="main-menu-right site-menu-style">
              <li>
                <Link to="/wardrobe">Wardrobe</Link>
              </li>
              <li>
                <Link to="/image-search">Search by Image</Link>
              </li>
              <li>
                <Link to="/preloved">Pre-love Goods</Link>
              </li>
              { this.state.login?
              
                <li>
                <Link  to="/login">Login</Link>
                </li> 
                :
                <li>
                <Link onClick={this.logout} to="/login">Logout</Link>
                </li>
             
              }
          
            </ul>
          </div>
        
        </header>
      </div>
    );
  }
 
}
export default Header;
