import $ from "jquery"
import "./libs/slick.min.js"
import Masonry from "masonry-layout"


import "./helpers.js";
import './modules/menu';
import './modules/modal-blog';
import './modules/galerie';
import './modules/forms';

/* slider component */
$(document).ready(function() {
    $('.slider-component').slick({
        slidesToShow: 2,
        slidesToScroll: 2,
        autoplaySpeed: 2000,
        infinite: true,
        autoplay: false,
        arrows: true,
        dots: true,
        centerMode: true,
        variableWidth: true,
        nextArrow: $('#sliderNext'),
        prevArrow: $('#sliderPrev'),
      
        responsive: [{
                breakpoint: 832,
                settings: {
                    arrows: true,
                    dots: true,
                    autoplay: false,
                    nextArrow: $('#sliderNext'),
                    prevArrow: $('#sliderPrev'),
                    slidesToShow: 1,
                    slidesToScroll: 1,
                    centerMode: true,
                    variableWidth: true,
                }
            }
        ]
    });

});

var grid = document.querySelector('.evenement-wrapper-component');
if(grid){
    var msnry = new Masonry( grid, {
        itemSelector: '.grid-item',
      });
}

//extra css for inscription page footer
if(document.querySelector(".inscription-page")){
    document.querySelector('.footer-component').style.marginTop = "auto"
}