export const classes = {
    active: 'active',
    hasFocus: 'has-focus',
    hidden: 'is-hidden',
    item: 'item',
    isMenuOpen: 'is-menu-open',
    isNotEmpty: 'is-not-empty',
    jsNotScrolledDown: 'on-top',
  };
  
  export const device = () => {
    let device = null;
  
    if (window.innerWidth < 768) {
      device = 'mobile';
    } else if (window.innerWidth >= 768 && window.innerWidth < 1200) {
      device = 'tablet';
    } else {
      device = 'desktop';
    }
  
    return device;
  };
  