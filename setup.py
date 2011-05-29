#!/usr/bin/env python

from distutils.core import setup

import djangobook

setup(
    name = 'djangobook',
    version = djangobook.__version__,
    description = '',
    author = '',
    author_email = '',
    url = 'http://github.com/pythonforfacebook/djangobook',
    packages = ['djangobook', 'djangobook.migrations', 'djangobook.templatetags'],
    package_data = {
        'djangobook': ['templates/*']
    }
)
