UNIT_TESTS = $(shell find ./quilljs/static/quilljs/js/test -name "*.js")
JS_FILES = $(shell find ./quilljs/static -name "*.js" -not -path "./quilljs/static/quilljs/js/test/*.js" -not -path "./quilljs/static/quilljs/js/build/*")
PY_FILES = $(shell find ./quilljs -name "*.py")

test:
	flake8 --ignore=E501 $(PY_FILES)
	./node_modules/.bin/jshint $(JS_FILES) $(UNIT_TESTS)
ifeq ($(CI),true)
	./node_modules/.bin/browserify -t coverify $(UNIT_TESTS) | ./node_modules/.bin/testling
else
	./node_modules/.bin/browserify -t coverify $(UNIT_TESTS) | ./node_modules/.bin/testling | ./node_modules/.bin/faucet
endif

docs:
	rm -rf out
	jsdoc quilljs/static/quilljs/js/ README.md

coverage:
	./node_modules/.bin/browserify -t coverify $(UNIT_TESTS) | ./node_modules/.bin/testling | ./node_modules/.bin/coverify

build:
	rm -f quilljs/static/quilljs/js/build/quilljs-django.js
	rm -f quilljs/static/quilljs/js/build/quilljs-django.min.js
	./node_modules/.bin/browserify $(JS_FILES) -o quilljs/static/quilljs/js/build/quilljs-django.js
	./node_modules/.bin/uglifyjs quilljs/static/quilljs/js/build/quilljs-django.js > quilljs/static/quilljs/js/build/quilljs-django.min.js

watch:
	./node_modules/.bin/watchify $(JS_FILES) -o quilljs/static/quilljs/js/build/quilljs-django.min.js
