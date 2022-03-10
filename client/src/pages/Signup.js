import React, { Component,useState } from "react";
import { Link,Redirect } from 'react-router-dom';
import axios from "axios";

function Signup() {
    
      const[firstName,setfirstName] = useState([]);
      const[lastName,setlastName] = useState([]);
      const[email,setemail] = useState([]);
      const[password,setpassword] = useState([]);

     async function sigup() {
        
        const det = {firstName,lastName,email,password}
        console.warn(det)
        
        let result = await fetch("http://localhost:2000/api/signup",{
          method:'POST',
          headers:{
            "Content-Type": 'application/json',
            "Accept":'application/json'
          },
          body:JSON.stringify({
            firstName: firstName,
            lastName: lastName,
            email: email,
            password: password
          })
        })
        result= await result.json()
        
      }
      return (
            <div>
                <section>
        <div className="container-fluid cona  ">
          <div className="row wmar2">
            <div className="col-lg-4 col-md-4 colred1">
              <div className="sip">
                <h1 className="colh ">Welcome!</h1>
                <h3 className="colh textsg">To keep connected with us please login your personal info</h3>
                <Link to="/login" className="sbtn btn btn-default">SIGN IN</Link>
              </div>
            </div>
            <div className="col-lg-8 col-md-8 textal1  ">
              <h1 className="signcol">Create Account</h1>
              <form>
                <div><input className="em" type="text" onChange={(e)=> setfirstName(e.target.value)} placeholder="FirstName"/></div>
                <div><input className="em" type="text" onChange={(e)=> setlastName(e.target.value)} placeholder="LastName"/></div>
                <div><input className="em" type="text" onChange={(e)=> setemail(e.target.value)} placeholder="Email"/></div>
                <div><input className="em" type="text" onChange={(e)=> setpassword(e.target.value)} placeholder="Password" /></div>
                
              </form>
                <Link onClick={sigup} className="fbtn btn btn-default">SIGN UP</Link>
            </div>
          </div></div></section>
            </div>
        );
    
}
export default Signup;
