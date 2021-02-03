import Masonry from "masonry-layout"
import $ from "jquery"
imagesLoaded.makeJQueryPlugin( $ );

/* plane color footer background in galerie and evenements pages */
document.addEventListener('turbolinks:load', function(){
    if(document.querySelector(".galerie-component")){
        $('.evenement-wrapper-component').imagesLoaded( function() {
            var msnry = new Masonry( document.querySelector('.evenement-wrapper-component'), {
                itemSelector: '.grid-item',
            });
        })
        document.querySelector('.footer-component').style.background = "#22262a"
        document.querySelector('.footer-component').style.padding = "50px 0"
    
        document.querySelector('.footer-component').style.background = "#22262a"
        if(document.querySelectorAll('.photo-item').length === 3){
            document.querySelector('.footer-component').style.padding = "100px 50px"
        }
    }
})