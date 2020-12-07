// Get the modal
var modal = document.querySelector(".modal-wrapper");

// Get the image and insert it inside the modal - use its "alt" text as a caption
var img = document.getElementById("open");
var modalImg = document.getElementById("modal-content");
var captionText = document.getElementById("caption");

if(modal){
    img.onclick = function(){
        modal.style.opacity = 1;
        modal.style.zIndex = 1;
        modalImg.src = this.src;
        captionText.innerHTML = this.alt;
      }
      
      // Get the <span> element that closes the modal
      var span = document.getElementsByClassName("close")[0];
      
      // When the user clicks on <span> (x), close the modal
      span.onclick = function() {
        modal.style.opacity = 0;
        modal.style.zIndex = -1;
      }
}