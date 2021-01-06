import { classes } from "../helpers";

export default (() => {
  const instances = [];
  const forms = [...document.querySelectorAll('form')];

  class Form {
    constructor(form) {
      this.form = form;
      this.fields = [...this.form.querySelectorAll('input:not([type="hidden"]), textarea, select')];

      this.bindEvents();
    }

    bindEvents() {
      this.fields.forEach(item => item.addEventListener('input', this.changeHandler));
      this.fields.forEach(item => item.addEventListener('focusin', this.focusHandler));
      this.fields.forEach(item => item.addEventListener('focusout', this.focusHandler));
    }

    changeHandler(e) {
      const target = e.currentTarget;

      if (target.value !== '') {
        target.parentNode.querySelector('.form-label').classList.add('is-not-empty');

      } else {
        target.parentNode.querySelector('.form-label').classList.remove('is-not-empty');
      }
    }

    focusHandler(e) {
      const target = e.target.closest('div');
      const targetClassList = [...target.classList];

      if (targetClassList.indexOf('has-focus') > -1) {
        target.classList.remove(classes.hasFocus);
      } else {
        target.classList.add(classes.hasFocus);
      }
    }
  }

  return forms.map(item => instances.push(new Form(item)));
})();
