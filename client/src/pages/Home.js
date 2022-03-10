import React, { Component, useEffect, useState } from "react";
import { Helmet } from "react-helmet";
import axios from "axios";
import $ from 'jquery';
import { Link , Redirect} from "react-router-dom";

function Home(){

  const eventApiUrl = "http://localhost:2000/api/products/eid-wear";
  const [casualShirts, setCasualShirts] = useState([]);
  //function to get api data
  const getCasualShirts = () => {
    const response = axios.get(eventApiUrl).then((response) => {
      console.warn(response.data);
      setCasualShirts(response.data.products);
      console.log(response.data);
      console.log(casualShirts);
    });
  };
  
 
  useEffect(() => {
    getCasualShirts();
    //getBrideDresses();
    //An array of assets
    let scripts = [
      { src: "js/bootstrap.min.js" },
      { src: "js/jquery.magnific-popup.min.js" },
      { src: "js/jquery.magnific-popup.min.js" },
      { src: "js/owl.carousel.min.js" },
      { src: "js/isotope.pkgd.min.js" },
      { src: "js/circle-progress.min.js" },
      { src: "js/main.js" },
    ];
    $('.icon-wishlist').on('click', function(){
      $(this).toggleClass('in-wishlist');
      });
    //Append the script element on each iteration
    scripts.map((item) => {
      const script = document.createElement("script");
      script.src = item.src;
      script.async = true;
      document.body.appendChild(script);
    });
  }, []);
async function addToWishlist(pro_id)
{
  const tokenData = localStorage.getItem("login");
  const user = JSON.parse(tokenData);
    
  let token= "Bearer " + user.store
  let result = await fetch('http://localhost:2000/api/user/wishlist/add-to-wishlist', {
        method: "POST",
        headers:{
          "Content-Type": 'application/json',
          "Accept":'application/json',
          'Authorization' : token
        },
        body:JSON.stringify({
          
          wishlistItems:{
            product: pro_id
            }
        })
    })
    result= await result.json()
    alert(result.message)
}
    return(
            <div>
         
        <section className="hero-section">
          <div className="hero-social-links">
            <a href="#"><i className="fa fa-pinterest" /></a>
            <a href="#"><i className="fa fa-facebook" /></a>
            <a href="#"><i className="fa fa-twitter" /></a>
           
          </div>
          
          <div className="hero-slider owl-carousel">
            <div className="hero-slider-item set-bg" data-setbg="img/slider-bg-1.png">
              <div className="hs-content">
                <div className="container">
                  <h2>ShopSpot</h2>
                 
                </div>
              </div>
            </div>
            <div className="hero-slider-item set-bg" data-setbg="img/slider-bg-1.png">
              <div className="hs-content">
                <div className="container">
                  <h2>ShopSpot</h2>
                </div>
              </div>
            </div>
          </div>
        </section>
        <section className="quote-section">
          <div className="container">
            <div className="quote-text text-center">
              <p>"Fashion is about dressing according to what’s fashionable. Style is more about being yourself."</p>
              <h3>—Oscar de la Renta</h3>
            </div>
          </div>
        </section>
        <div className="portfolio-section">
          <div className="portfolio-gallery">
            <div className="portfolio-item set-bg" data-setbg="img/works/1.jpg">
              <a href="img/works/1.jpg" className="portfolio-view">loadmore</a>
            </div>
            <div className="portfolio-item --disable">
            </div>
            <div className="portfolio-item set-bg" data-setbg="img/works/2.jpg">
              <a href="img/works/2.jpg" className="portfolio-view">loadmore</a>
            </div>
            <div className="portfolio-item --big set-bg" data-setbg="img/works/6.jpg">
              <a href="img/works/6.jpg" className="portfolio-view">loadmore</a>
            </div>
            <div className="portfolio-item set-bg" data-setbg="img/works/3.jpg">
              <a href="img/works/3.jpg" className="portfolio-view">loadmore</a>
            </div>
            <div className="portfolio-item set-bg" data-setbg="img/works/5.jpg">
              <a href="img/works/5.jpg" className="portfolio-view">loadmore</a>
            </div>
            <div className="portfolio-item set-bg" data-setbg="img/works/4.jpg">
              <a href="img/works/4.jpg" className="portfolio-view">loadmore</a>
            </div>
            <div className="portfolio-item set-bg" data-setbg="img/works/7.jpg">
              <a href="img/works/7.jpg" className="portfolio-view">loadmore</a>
            </div>
            <div className="portfolio-item set-bg" data-setbg="img/works/8.jpg">
              <a href="img/works/8.jpg" className="portfolio-view">loadmore</a>
            </div>
            <div className="portfolio-item set-bg" data-setbg="img/works/9.jpg">
              <a href="img/works/9.jpg" className="portfolio-view">loadmore</a>
            </div>
            <div className="portfolio-item set-bg" data-setbg="img/works/10.jpg">
              <a href="img/works/10.jpg" className="portfolio-view">loadmore</a>
            </div>
            <div className="portfolio-item set-bg" data-setbg="img/works/11.jpg">
              <a href="img/works/11.jpg" className="portfolio-view">loadmore</a>
            </div>
          </div>
        </div>
        <section className="about-secton">
          <div className="container">
            <img src="img/about-img.jpg" className="about-img" alt="" />
            <div className="row">
              <div className="col-lg-7 about-text">
                <h2>Fashions fade, style is eternal</h2>
                <p>Maecenas facilisis facilisis consequat. Curabitur fringilla pellentesque neque, imperdiet effic-tur urna gravida vel. Cras augue diam, sollicitudin sit amet felis ut, eleifend faucibus dui. Proin euismod suscipit lacus, et scelerisque nisi aliquam anunc feugiat mattis quam, ut luctus enim ultrices at. Maecenas facilisis facilisis consequat. Curabitur fringilla pellentesque neque, imperdiet efficitur urna gravida vel. Cras augue diam, sollicitudin sit amet felis ut, eleifend faucibus dui. Proin euismod suscipit lacus, et scelerisque nisi aliquam a. Nunc feugiat mattis quam, ut luctus enim ultrices at.</p>
                <img src="img/signature.png" alt="" />
              </div>
            </div>
          </div>
          <div className="about-img-box-warp">
            <div className="container-fluid">
              <div className="row">
                <div className="col-lg-6 p-0">
                  <div className="about-img-box">
                    <img src="img/image-box.jpg" alt="" />
                  </div>
                </div>
                <div className="col-lg-6  d-lg-flex align-items-center p-0">
                  <div className="about-text-box-warp">
                    <div className="about-text">
                      <h2>The joy of dressing is an art</h2>
                      <p>Curabitur fringilla pellentesque neque, imperdiet efficitur urna gravida vel. Cras augue diam, sollicitudin sit amet felis ut, eleifend faucibus dui. Proin euismod suscipit lacus, et scelerisque nisi aliquam anunc feugiat mattis quam, ut luctus enim ultrices at. Maecenas facilisis facilisis consequat. Curabitur fringilla pellentesque neque, imperdiet efficitur urna gravida vel. Cras augue diam, sollicitudin sit amet felis ut, eleifend faucibus dui. Proin euismod suscipit lacus, et scelerisque nisi aliquam a. Nunc feugiat mattis quam, ut luctus enim ultrices at.</p>
                    </div>
                  </div>
                </div>
              </div>
            </div>
          </div>
        </section>
        <section>
        <div className="container mevent">
        <h2 className="catetitle">Select a Category</h2>
          <div className="row">
          <div className="col-lg-4 col-sm-4">
        <div style={{width: '100%'}} className="portfolio-item set-bg" data-setbg="img/works/8.jpg">
          <Link  to={{
              pathname:'/events',
              state: {
                data:"man"
              }}} className="portfolio-view2">
              Men
            </Link>
             
          </div>
          </div>
          <div className="col-lg-4 col-sm-4">
          <div  style={{width: '100%'}} className="portfolio-item set-bg" data-setbg="img/works/5.jpg">
          <Link  to={{
              pathname:'/events',
              state: {
                data:"women"
              }}} className="portfolio-view2">
              Women
            </Link>
          </div>
          </div>
          <div className="col-lg-4 col-sm-4">
          <div  style={{width: '100%'}} className="portfolio-item set-bg" data-setbg="img/works/kids.jpg">
            <Link  to={{
              pathname:'/events',
              state: {
                data:"kids"
              }}} className="portfolio-view2">
              Kids
            </Link>
          </div>
          </div>
        </div>
        </div>
    
        </section>
      </div>
              
               
            
        )
    }


export default Home