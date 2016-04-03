var gulp = require('gulp');
var concat = require('gulp-concat');
var uglify = require('gulp-uglify');
var rename = require('gulp-rename');
var connect = require('gulp-connect');
var browserify = require('browserify');
var source = require('vinyl-source-stream')

gulp.task('minify', function(){
    return gulp.src('js/*.js')
        .pipe(concat('main.js'))
        .pipe(gulp.dest('dist'))
        .pipe(rename('main.min.js'))
        .pipe(uglify())
        .pipe(gulp.dest('dist/js'))
})

gulp.task('browserify', function() {
    return browserify('./js/app.js')
        .bundle()
        .pipe(source('main.js'))
        .pipe(gulp.dest('dist/js'))
})

gulp.task('connect', function () {
    connect.server({
        root: 'public',
        port: 4000
    })
})

gulp.task('watch', function() {
    gulp.watch('../static/**/*.js', ['browserify'])
})

gulp.task('default', ['connect', 'watch'])