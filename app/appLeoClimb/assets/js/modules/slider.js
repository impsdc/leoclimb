import $ from "jquery"
$(document).on('turbolinks:load', function(){
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
})