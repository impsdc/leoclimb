export default class Article {
  constructor(article) {
    this.article = article
    this.img = article.querySelector("#open"); 
    this.modalImg = article.querySelector("#modal-content");
    this.modal = article.querySelector(".modal-wrapper");
    this.bindEvents(this.article, this.img, this.modal, this.modalimg);
  }

  bindEvents(article, img, modal, modalimg) {
    this.img.addEventListener('click', function(){

      article.querySelector(".modal-wrapper").style.zIndex = 1;
      article.querySelector(".modal-wrapper").style.opacity = 1;
      article.querySelector("#modal-content").src = img.src;
  
      let span = article.getElementsByClassName("close")[0];
        
      // When the user clicks on <span> (x), close the modal
      span.onclick = function() {
        modal.style.opacity = 0;
        modal.style.zIndex = -1;
      }
  
      article.querySelector('.modal-wrapper').onclick = function() {
        modal.style.opacity = 0;
        modal.style.zIndex = -1;
      }
  });   
  }
};