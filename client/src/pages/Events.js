import React, { Component, useEffect, useState } from "react";
import { Helmet } from "react-helmet";
import { Link, useParams } from "react-router-dom";
import axios from "axios";
import Portfolio from "../pages/Products";
import Products from "./Products"

function Events(props) {
  useEffect(() => {
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
    //Append the script element on each iteration
    scripts.map((item) => {
      const script = document.createElement("script");
      script.src = item.src;
      script.async = true;
      document.body.appendChild(script);
    });
  }, []);
  let cat = props.location.state.data;
  return (
    <div>
      
      <div className="portfolio-page-section">
        <div className="container">
          <ul className="portfolio-filter">
            <li className="filter all active" data-filter="*">
              All
            </li>
            <li className="filter" data-filter=".collections">
              Collections
            </li>
            <li className="filter" data-filter=".models">
              Models
            </li>
            <li className="filter" data-filter=".ss19">
              SS19
            </li>
            <li className="filter" data-filter=".fw19">
              Fw19
            </li>
          </ul>
        </div>
        <div className="portfolio-gallery">
          <div className="portfolio-item set-bg" data-setbg="img/works/2.jpg">
            
            <Link  to={{
              pathname:'/products',
              state: {
                data:cat+"/eid-wear"
              }}} className="portfolio-view2">
              Eid Wear
            </Link>
          </div>
          <div className="portfolio-item --disable"></div>
          <div className="portfolio-item set-bg" data-setbg="img/works/2.jpg">
             
            <Link  to={{
              pathname:'/products',
              state: {
                data:"eid-wear"
              }}} className="portfolio-view2">
              Eid Wear
            </Link>
            {/* <Portfolio eventType={"Men Shalwar"} /> */}
          </div>
          <div
            className="portfolio-item --big set-bg"
            data-setbg="img/works/6.jpg"
          >
            <Link to={{
              pathname:'/products',
              state: {
                data:cat+"casual-wear"
              }}}  className="portfolio-view2">
              Bride Barat Dress
            </Link>
          </div>
          <div className="portfolio-item set-bg" data-setbg="img/works/3.jpg">
            <Link to={{
              pathname:'/products',
              state: {
                data:cat+"/casual-wear"
              }}}   className="portfolio-view2">
              Men Causal
            </Link>
          </div>
          <div className="portfolio-item set-bg" data-setbg="img/works/5.jpg">
            <Link to="/women-party" className="portfolio-view2">
              Women Party Wear
            </Link>
          </div>
          <div className="portfolio-item set-bg" data-setbg="img/works/4.jpg">
            <Link to="/products" className="portfolio-view2">
              Bride Mehndi Dress
            </Link>
          </div>
          <div className="portfolio-item set-bg" data-setbg="img/works/8.jpg">
            <Link to="/products" className="portfolio-view2">
              Men Barat Wear
            </Link>
          </div>
          <div className="portfolio-item set-bg" data-setbg="img/works/9.jpg">
            <Link to="/products" className="portfolio-view2">
              Bride Walima Dress
            </Link>
          </div>
          <div className="portfolio-item set-bg" data-setbg="img/works/10.jpg">
            <Link to="/party-wear" className="portfolio-view2">
              Men Party Wear
            </Link>
          </div>
          <div className="portfolio-item set-bg" data-setbg="img/works/11.jpg">
            <Link to={{
              pathname:'/products',
              state: {
                data:"formal-wear"
              }}}   className="portfolio-view2">
              Men Formal Wear
            </Link>
          </div>
          <div
            className="portfolio-item --big --wide set-bg fw19"
            data-setbg="img/works/12.jpg"
          >
            <Link to="/products" className="portfolio-view2">
              Groom Barat Dress
            </Link>
          </div>
          <div
            className="portfolio-item set-bg fw19"
            data-setbg="img/works/13.jpg"
          >
            <Link to="/eid-wear" className="portfolio-view2">
              Men Eid Wear
            </Link>
          </div>
          <div
            className="portfolio-item set-bg fw19"
            data-setbg="img/works/15.jpg"
          >
            <Link to="/products" className="portfolio-view2">
              Groom Mehndi Wear
            </Link>
          </div>
          <div
            className="portfolio-item set-bg fw19"
            data-setbg="img/works/16.jpg"
          >
            <Link to="/products" className="portfolio-view2">
              Groom Walima Wear
            </Link>
          </div>
          <div className="portfolio-item set-bg fw19" data-setbg="">
            <Link to="/products" className="portfolio-view2"></Link>
          </div>
          <div className="portfolio-item set-bg fw19" data-setbg="">
            <Link to="/products" className="portfolio-view2"></Link>
          </div>
        </div>
      </div>
    
    </div>
  );
}
export default Events;
