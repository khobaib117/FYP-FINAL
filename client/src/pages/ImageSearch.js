import React, { Component, useEffect, useState } from "react";
import { Link } from "react-router-dom";
import axios from "axios";

function ImageSearch() {
  const [picture, setPicture] = useState({});
  const [casualShirts, setCasualShirts] = useState([]);
  const [queryImage, setQueryImage] = useState("");
 
  const onImageChange = (event) => {
    setPicture({
      /* contains the preview, if you want to show the picture to the user
           you can access it with this.state.currentPicture
       */
      picturePreview: URL.createObjectURL(event.target.files[0]),
      /* this contains the file we want to send */
      pictureAsFile: event.target.files[0],
    });
    if (event.target.files && event.target.files[0]) {
      let img = event.target.files[0];
      setQueryImage(URL.createObjectURL(img));
    }
  };
  useEffect(() => {
    
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
    //Append the script element on each iteration
    scripts.map((item) => {
      const script = document.createElement("script");
      script.src = item.src;
      script.async = true;
      document.body.appendChild(script);
    });
  }, []);
  const uploadPicture = (e) => {
    setPicture({
      /* contains the preview, if you want to show the picture to the user
           you can access it with this.state.currentPicture
       */
      picturePreview: URL.createObjectURL(e.target.files[0]),
      /* this contains the file we want to send */
      pictureAsFile: e.target.files[0],
    });
  };

  const setImageAction = async (event) => {
    event.preventDefault();

    const formData = new FormData();
    formData.append("queryImage", picture.pictureAsFile);

    console.log(picture.pictureAsFile);

    for (var key of formData.entries()) {
      console.log(key[0] + ", " + key[1]);
    }

    const data = await fetch("http://localhost:2000/api/image-search", {
      method: "post",
      body: formData,
    });
    
    const uploadedImage = await data.json();
    
    setCasualShirts(uploadedImage.suggestedProducts);
    console.log(casualShirts);
    if (uploadedImage) {
      console.log("Successfully uploaded image");
    } else {
      console.log("Error Found");
    }
  };

  return (
    <div className="content landing">
       <div className="shop-section">
        <div className="portfolio-gallery">
        <div className="portfolio-item set-bg">
        <div class="wrapper">
        <div class="file-upload">
            <input type="file"
             class="imagesearch2"
             type="file"
             name="query_img"
             onChange={onImageChange} />
            <i class="fa fa-arrow-up"></i>
        </div>
        </div>
            </div>

          <div className="portfolio-item set-bg" >
             <img class="img-size" src={queryImage} />
          </div>
        </div>
    </div>
    <div className="load ">
    <a onClick={setImageAction} className="load-more">
      Search
    </a>
    </div>
      <section className="shop-section">
        <div className="container">
          <div className="row">
            {casualShirts.map((suggestedProducts) => {
              return (
                <div className="box col-lg-3 col-sm-6">
                  <div className="shop-item">
                    <img src={suggestedProducts.imageLink} alt="" />
                   
                    {/* <img src="img/shop/1.jpg" alt="" /> */}
                    <h3>{suggestedProducts.title}</h3>
                    <h6>{suggestedProducts.price}</h6>
                    <a
                      href={suggestedProducts.productLink}
                      className="add-card"
                      target="_blank"
                    >
                      See Details
                    </a>
                  </div>
                </div>
              );
            })}
          </div>
        </div>
      </section>
      </div>
  );
  }
//}
export default ImageSearch;
