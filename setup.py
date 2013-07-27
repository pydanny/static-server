#!/usr/bin/env python

import os
import sys

import static

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

if sys.argv[-1] == 'publish':
    os.system('python setup.py sdist upload')
    sys.exit()

readme = open('README.rst', 'rt').read()
history = open('HISTORY.rst', 'rt').read()

setup(
    name='static',
    version=static.__version__,
    description='A simple WSGI way to serve static (or mixed) content.',
    long_description=readme + '\n\n' + history,
    author='Daniel Greenfeld',
    author_email='pydanny@gmail.com',
    url='https://github.com/pydanny/staticserve',
    license="LGPL",
    py_modules=['static'],
    include_package_data=True,
    zip_safe=False,
    keywords='wsgi web http static content webapps',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: GNU Library or Lesser General Public License (LGPL)',
        'Natural Language :: English',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.3',
        'Topic :: Software Development :: Libraries',
        'Topic :: Utilities'
    ],
    #test_suite='tests',
)