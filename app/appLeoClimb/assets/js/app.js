setTimeout(() => document.body.classList.add('render'), 50);
import $ from "jquery"
import "./libs/slick.min.js"
import Masonry from "masonry-layout"

import "./helpers.js";
import './modules/menu';
import './modules/modal-blog';
import './modules/galerie';
import './modules/forms';

$(document).ready(function() {

    // Set up two Deferred objects, to track images and fonts.
    var images_loaded = $.Deferred()

    // When both promises complete, redo the Masonry layout.
    $.when(images_loaded).done(function() {
        // Try commenting out this line; without it, masonry won't find any images
        // and the layout should be standard HTML.
        var grid = document.querySelector('.evenement-wrapper-component');
        if(grid){
            var msnry = new Masonry( grid, {
                itemSelector: '.grid-item',
            });
        }

    });

    // Deal with the image loading process using Masonry's imagesLoaded plugin.
    imagesLoaded( Array.prototype.map.call(document.images, img => img.src), function() {
      document.body.classList.remove("loading")
      images_loaded.resolve();
    });
});

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

//extra css for inscription page footer
if(document.querySelector(".inscription-page")){
    document.querySelector('.footer-component').style.marginTop = "auto"
}