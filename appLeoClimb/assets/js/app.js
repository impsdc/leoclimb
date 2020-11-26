import $ from "jquery"
import "./libs/slick.min.js"


import "./helpers.js";
import './modules/menu';
import './modules/carrousel';

$(document).ready(function() {
    $('.slider-component').slick({
        slidesToShow: 2,
        slidesToScroll: 2,
        autoplaySpeed: 2000,
        infinite: true,
        autoplay: false,
        arrows: true,
        dots: true,
        variableWidth: true,
        nextArrow: $('#sliderNext'),
        prevArrow: $('#sliderPrev'),
      
        responsive: [{
                breakpoint: 992,
                settings: {
                    arrows: true,
                    autoplay: false,
                    dots: true,
                    nextArrow: $('#sliderNext'),
                    prevArrow: $('#sliderPrev'),
                    slidesToShow: 2,
                    centerMode: true,
                    variableWidth: false,
                }
            },
            {
                breakpoint: 832,
                settings: {
                    arrows: true,
                    dots: true,
                    autoplay: false,
                    nextArrow: $('#sliderNext'),
                    prevArrow: $('#sliderPrev'),
                    slidesToShow: 1,
                    centerMode: false,
                    variableWidth: false,
                }
            }
        ]
});

});