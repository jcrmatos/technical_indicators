#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Technical analysis indicators."""

# Python 3 compatibility
from __future__ import (absolute_import, division, print_function,
                        #unicode_literals
                        )
# The above unicode_literals import prevents setup.py from working.
# It seems to be a bug in setuptools.
# py2exe build also does not work if it is unremarked.

import sys
from os import path

sys.path.insert(1, path.dirname(__file__))  # add to PYTHONPATH

AUTHOR = 'Joao Matos'
EMAIL = 'jcrmatos@gmail.com'
COPYRIGHT = 'Copyright 2014 ' + AUTHOR

NAME = 'technical_indicators'
SCRIPT = NAME + '/technical_indicators.py'

VERSION = '0.0.0'
CHANGE_LOG_FILE = 'ChangeLog.txt'
if path.isfile(CHANGE_LOG_FILE):  # if file exists
    with open(CHANGE_LOG_FILE) as f:
        VERSION = f.readline().split()[0]

LONG_DESC = DESC = ''
README_FILE = 'README.txt'
if path.isfile(README_FILE):  # if file exists
    with open(README_FILE) as f:
        LONG_DESC = f.read()
        DESC = LONG_DESC.split('\n')[3]

LICENSE = 'GNU General Public License v2 or later (GPLv2+)'
URL = 'https://github.com/jcrmatos/technical_indicators'
KEYWORDS = 'technical analysis indicators'
CLASSIFIERS = ['Development Status :: 4 - Beta',
               'Environment :: Console',
               'Intended Audience :: End Users/Desktop',
               'Intended Audience :: Developers',
               'Natural Language :: English',
               'License :: OSI Approved ::' +
               ' GNU General Public License v2 or later (GPLv2+)',
               'Operating System :: OS Independent',
               'Programming Language :: Python',
               'Programming Language :: Python :: 2.7',
               'Topic :: Other/Nonlisted Topic',
               #'Private :: Do Not Upload'  # to prevent PyPI publishing
               ]

LICENSE_FILE = 'LICENSE.txt'
AUTHORS_FILE = 'AUTHORS.txt'

DATA_FILES = [LICENSE_FILE, README_FILE, AUTHORS_FILE, CHANGE_LOG_FILE]

DATA_FILES_PY2EXE = [('', [NAME + '/' + LICENSE_FILE]),
                     ('', [NAME + '/' + README_FILE]),
                     ('', [NAME + '/' + AUTHORS_FILE]),
                     ('', [NAME + '/' + CHANGE_LOG_FILE])]

DATA_FILES_CXF = [NAME + '/' + LICENSE_FILE, NAME + '/' + README_FILE,
                  NAME + '/' + AUTHORS_FILE, NAME + '/' + CHANGE_LOG_FILE]
