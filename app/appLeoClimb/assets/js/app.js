var Turbolinks = require("turbolinks")
Turbolinks.start()

import "./libs/slick.min.js"
import './modules/slider'
import './modules/menu';
import Article from './modules/modal-blog';
import './modules/galerie';
import Form from './modules/forms'; 

document.addEventListener('turbolinks:load', function(){
    if(document.querySelector('.inscription-page')){
        document.querySelector('.footer-component').style.marginTop = "auto"
        const instances = [];
        const forms = [...document.querySelectorAll('form')];
        forms.map(item => instances.push(new Form(item)));
    }
})

document.addEventListener('turbolinks:load', function(){
    if(document.querySelector('.actualite-component')){
        const instances = [];
        const article = [...document.querySelectorAll('.single-article')];
        article.map(item => instances.push(new Article(item)));
    }
})