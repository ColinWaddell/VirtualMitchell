module.exports = function (grunt) {
    grunt.initConfig({
        watch: {
            files: ['parts/static/sass/**/*.{scss,sass}'],
            tasks: ['sass']
        },

        sass: {
            dist: {
                files: {
                    'parts/static/css/parts.css': 'parts/static/sass/manifest.scss',
                    'ncr/static/css/ncr.css': 'ncr/static/sass/manifest.scss',
                    'common/static/css/cstracker.css': 'common/static/scss/manifest.scss'
                }
            }
        },

        browserSync: {
            dev: {
                bsFiles: {
                    src : [
                        'parts/static/css/*.css',
                        'parts/static/js/*.js',
                        '**/*.py',
                        '**/*.html'
                    ]
                },
                options: {
                    watchTask: true,
                    proxy: 'localhost:8000',
                    online: true,
                    open: false,
                    reloadDelay: 1500
                }
            }
        },

        uglify: {  
            options: {  
                compress: false 
            },  
            applib: {  
                src: [
                    'node_modules/jquery/dist/jquery.js',
                    'node_modules/popper.js/dist/umd/popper.js',
                    'node_modules/bootstrap/dist/js/bootstrap.js'
                ],  
                dest: 'common/static/js/cstracker.js'  
            }  
        },

        shell: {
            djangoRun: {
                command: 'env/bin/python manage.py runserver',
                options: {
                  stdout: true,
                  failOnError: true,
                  async: true
                }
            },

            djangoRunWindows: {
                command: 'env\\Scripts\\python.exe manage.py runserver',
                options: {
                  stdout: true,
                  failOnError: true,
                  async: true
                }
            }
        }
    });

    // load npm tasks
    grunt.loadNpmTasks('grunt-contrib-sass');
    grunt.loadNpmTasks('grunt-contrib-watch');
    grunt.loadNpmTasks('grunt-browser-sync');
    grunt.loadNpmTasks('grunt-shell-spawn');
    grunt.loadNpmTasks('grunt-contrib-uglify');

    // define default task
    grunt.registerTask('default', ['shell:djangoRun', 'browserSync', 'watch']);
    grunt.registerTask('windows', ['shell:djangoRunWindows', 'browserSync', 'watch']);
};
