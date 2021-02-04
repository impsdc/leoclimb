import Masonry from "masonry-layout"
import $ from "jquery"
imagesLoaded.makeJQueryPlugin( $ );

/* let grid = document.querySelector('.evenement-wrapper-component');
if(grid){
    $('.evenement-wrapper-component').imagesLoaded( function() {
        document.body.classList.remove("loading")
                var msnry = new Masonry( grid, {
                    itemSelector: '.grid-item',
                });
    });

}else{
    $('section').imagesLoaded( function() {
        document.body.classList.remove('loading')
    });
} */

/* plane color footer background in galerie and evenements pages */
document.addEventListener('turbolinks:load', function(){
    if(document.querySelector(".galerie-component")){
        $('.evenement-wrapper-component').imagesLoaded( function() {
            var msnry = new Masonry( document.querySelector('.evenement-wrapper-component'), {
                itemSelector: '.grid-item',
            });
        })
        document.querySelector('.footer-component').style.background = "#22262a"
    }
})