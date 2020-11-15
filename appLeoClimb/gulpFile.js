const gulp = require('gulp');
const sass = require('gulp-sass');
const rename = require('gulp-rename');
const browserSync = require('browser-sync').create();


// Créer la tâche Browser Sync
gulp.task("browser-sync", function() {
    browserSync.init({
      proxy: "http://127.0.0.1:8000/", // Pensez à mettre votre URL ici
      ghostMode: false,
      open: false,
      notify: false
    })
  })


gulp.task("style", function(){

    return gulp.src('./assets/scss/app.scss')

    .pipe(sass({outputStyle:'compressed'}))
    .pipe(rename('app.css'))
    .pipe(gulp.dest('./static/'))

    .pipe(browserSync.reload({ stream: true }))

}) 


gulp.task("watch", ["browser-sync"], function() {

    gulp.watch('./assets/scss/**/*.scss', ["style"], browserSync.reload);
    gulp.watch("./templates/*.html").on("change", browserSync.reload) 
    gulp.watch("./templates/admin/*.twig").on("change", browserSync.reload) 

});