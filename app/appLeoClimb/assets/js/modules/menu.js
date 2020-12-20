import { classes } from '../helpers';
import { debounce } from 'lodash';

export default (() => {
  const menuToggler = document.querySelector('.navbar-toggler');
  const nav = document.querySelector('.nav-component');
  const header = document.querySelector('.header-component');
  const body = document.querySelector('body');
  const html = document.documentElement;

  const clickHandler = () => {
    const height = nav.classList.contains(classes.active) ? 0 : window.innerHeight - (header.offsetHeight - 2);

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
    const height = nav.classList.contains(classes.active) ? window.innerHeight - (header.offsetHeight - 1) : 0;
    nav.style.maxHeight = `${height}px`;
  };

  const scrollHandler = () => {
    if (window.pageYOffset > header.offsetHeight) {
      body.classList.remove(classes.jsNotScrolledDown);
    } else {
      body.classList.add(classes.jsNotScrolledDown);
    }
  };

  const bindEvents = () => {
    scrollHandler();
    menuToggler.addEventListener('click', clickHandler);
    window.addEventListener('resize', resizeHandler);
    window.addEventListener('orientationchange', closeHandler);
    window.addEventListener('scroll', debounce(scrollHandler, 20));
  };

  return bindEvents();
})();
