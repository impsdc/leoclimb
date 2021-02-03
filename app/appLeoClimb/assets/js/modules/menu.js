import { classes } from '../helpers';
import { debounce } from 'lodash';
import $ from "jquery"
export default (() => {
  const menuToggler = document.querySelector('.navbar-toggler');
  const links = document.querySelectorAll('.nav-component ul li a');
  const nav = document.querySelector('.nav-component');
  const header = document.querySelector('.header-component');
  const html = document.documentElement;

  const clickHandler = () => {
    const height = nav.classList.contains(classes.active) ? 0 : window.innerHeight - (header.offsetHeight) + 5;

    menuToggler.classList.toggle(classes.active);
    nav.classList.toggle(classes.active);
    nav.style.maxHeight = `${height}px`;
    html.classList.toggle(classes.isMenuOpen);
  };

  const closeHandler = () => {
    menuToggler.classList.remove(classes.active);
    nav.classList.remove(classes.active);
    nav.style.maxHeight = 0;
    html.classList.remove(classes.isMenuOpen);
  };

  const resizeHandler = () => {
    const height = nav.classList.contains(classes.active) ? window.innerHeight - (header.offsetHeight) : 0;
    nav.style.maxHeight = `${height}px`;
  };

  const bindEvents = () => {
    menuToggler.addEventListener('click', clickHandler);
    links.forEach(element => {element.addEventListener("turbolinks:click", closeHandler)});
    window.addEventListener('resize', resizeHandler);
    window.addEventListener('orientationchange', closeHandler);
    $(document).on('turbolinks:load', function(){
      window.addEventListener('scroll', debounce(scrollHandler, 10)); 
    })
  };

const scrollHandler = () => {
    if (window.pageYOffset > document.querySelector('.header-component').offsetHeight) {
        document.querySelector('body').classList.remove(classes.jsNotScrolledDown);
      } else {
        document.querySelector('body').classList.add(classes.jsNotScrolledDown);
      }
  };
  return bindEvents();
})();
