/* plane color footer background in galerie and evenements pages */
if(document.querySelector('.galerie-component')){
    document.querySelector('.footer-component').style.background = "#22262a"
    document.querySelector('.footer-component').style.padding = "50px 0"
}

if(document.querySelector('.evenement-component')){
    document.querySelector('.footer-component').style.background = "#22262a"
    if(document.querySelectorAll('.photo-item').length === 3){
        document.querySelector('.footer-component').style.padding = "100px 50px"
    }
}

