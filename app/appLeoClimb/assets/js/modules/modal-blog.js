var items = document.querySelectorAll(".single-article");

items.forEach(element => {
  
  let img = element.querySelector("#open");
  let modalImg = element.querySelector("#modal-content");
  let captionText = element.querySelector("#caption");
  let modal = element.querySelector(".modal-wrapper");

  if(element){
  
    img.onclick = function(){
        modal.style.opacity = 1;
        modal.style.zIndex = 1;
        modalImg.src = this.src;
        captionText.innerHTML = this.alt;
      }
      
      // Get the <span> element that closes the modal
      let span = element.getElementsByClassName("close")[0];
      
      // When the user clicks on <span> (x), close the modal
      span.onclick = function() {
        modal.style.opacity = 0;
        modal.style.zIndex = -1;
      }

      element.querySelector('.modal-wrapper').onclick = function() {
        modal.style.opacity = 0;
        modal.style.zIndex = -1;
      }
  }
});
