module.exports = function (grunt) {
    grunt.initConfig({
        watch: {
            sass: {
                files: ['www/static/sass/**/*.{scss,sass}'],
                tasks: ['sass']
            },

            vue: {
                files: ['www/static/src/**/*.{vue,js}', ],
                tasks: ['browserify']
            }
        },

        sass: {
            dist: {
                files: {
                    'www/static/css/vm.css': 'www/static/sass/manifest.scss',
                }
            }
        },

        browserSync: {
            dev: {
                bsFiles: {
                    src : [
                        'www/static/css/*.css',
                        'www/static/js/*.js',
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
                dest: 'www/static/js/vm.js'  
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
        },

        browserify: {
            bundle: {
                src: 'www/static/src/index.js',
                dest: 'www/static/js/map.min.js'
            },
            options: {
                browserifyOptions: {
                    debug: false
                },
                transform: [
                    ["vueify", ]
                ]
            }
        }
    });

    // load npm tasks
    grunt.loadNpmTasks('grunt-contrib-sass');
    grunt.loadNpmTasks('grunt-contrib-watch');
    grunt.loadNpmTasks('grunt-browser-sync');
    grunt.loadNpmTasks('grunt-shell-spawn');
    grunt.loadNpmTasks('grunt-contrib-uglify');
    grunt.loadNpmTasks('grunt-browserify');

    // define default task
    grunt.registerTask('default', ['shell:djangoRun', 'browserSync', 'watch']);
    grunt.registerTask('windows', ['shell:djangoRunWindows', 'browserSync', 'watch']);
};
