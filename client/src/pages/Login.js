import React, { Component } from "react";
import { Link,Redirect } from 'react-router-dom';
import Header from '../Components/Header';
import axios from "axios";
export default class Login extends Component {
  constructor(props) {

    super(props);
    this.state={
        email : null,
        password: null,
        login: false,
        store: null
    }
    

}
componentDidMount (){

  this.storeCollector()
}
storeCollector () 
    {

        let store= JSON.parse(localStorage.getItem('login'));
       
        console.log('Here is store: ' + store);
        if (store && store.login)
        {
            this.setState({login:true,store:store})
        }
    }
async login ()
{
    console.log(this.state);
    let result = await fetch("http://localhost:2000/api/signin",{     
          method:'POST',
          headers:{
            "Content-Type": 'application/json',
            "Accept":'application/json'
          },
          body:JSON.stringify({
            email: this.state.email,
            password: this.state.password
          })
        })
        result= await result.json()
        console.warn(result.token)
        
        if (result.token==null)
                {
                    this.setState({login:false})
                    alert("Enter correct username and password!");
                }
                else {

                    localStorage.setItem('login', JSON.stringify({
                        login:true,
                        store:result.token
                    }))
                    sessionStorage.setItem('login','true');
                    
                    this.storeCollector ();
                    
                }
       
}
post ()
{
    
    let token= "Bearer " + this.state.store.store
    console.log(this.state.store.store);
    fetch('http://localhost:2000/api//user/wishlist', {
        method: "GET",
        headers: {
            'Authorization' : token
        },
    body:JSON.stringify(this.state.post)
    }).then((response)=> {
        response.json().then((result)=>{
            console.warn("result", result);
        })
    })
}
render() {

  if (this.state.login) {
    return (<Redirect to={'/'}/>
    )
  }
  

    return (
        
        <div>
          {  !this.state.login?
            
        <section>
        <div className="container-fluid cona  ">
          <div className="row wmar2">
           
            <div className="col-lg-8 col-md-8 textal  ">
              <h1 className="signcol">Sign in to ShopSpot</h1>
              
              <form>
                <div><input className="em" onChange={(event)=> {this.setState({email:event.target.value})}} type="text" placeholder="Email" /></div>
                <div><input className="em" onChange={(event)=> {this.setState({password:event.target.value})}} type="password" placeholder="Password"/></div>
                <p className="textb">Forgot your password?</p>
                
              </form>
              <button onClick={()=>{this.login()}} className="fbtn btn btn-default">Sign in</button>
            
          </div>
           
            <div className="col-lg-4 col-md-4 colred">
              <div className="sip">
                <h1 className="colh ">Hi, Friend!</h1>
                <h3 className="colh textsg">Enter your personal details and start your journey with us.</h3>
                <button className="sbtn btn btn-default"><Link to="/Signup">SIGN UP</Link></button>
              </div>
            </div>
          </div></div></section>
           :
           <div>
               <textarea onChange={(event)=>this.setState({post:event.target.value})}>
                     
               </textarea>
               <Link to="/about" onClick={()=>this.post()}>Post</Link>
                 
           </div>
            }
          </div>
    );
  }
}