'use strict';

var test = require('tape');
var QuilljsDjango = require('../quilljs-django.js');

test('QuilljsDjango constructor', function (t) {
    t.plan(3);

    t.throws(function () {
        new QuilljsDjango();
    });

    t.throws(function () {
        new QuilljsDjango('test');
    });

    t.throws(function () {
        new QuilljsDjango('test', '#test');
    });
});
