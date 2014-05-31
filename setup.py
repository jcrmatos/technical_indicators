#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Python 3 compatibility
from __future__ import (absolute_import, division, print_function,
                        unicode_literals)

import sys
from os import path
from setuptools import setup, find_packages
#import py2exe


from technical_indicators import (NAME, VERSION, DESC, LONG_DESC, LICENSE, URL,
                                  AUTHOR, EMAIL, KEYWORDS, CLASSIFIERS, SCRIPT,
                                  DATA_FILES, DATA_FILES_PY2EXE)


#PACKAGES = [NAME] # only used if find_packages() does not work

ENTRY_POINTS = {'console_scripts': ['technical_indicators=technical_indicators.technical_indicators:main'],
                #'gui_scripts': ['app_gui=technical_indicators.technical_indicators:start']
                }

PKG_DATA = dict(technical_indicators=DATA_FILES)
#PKG_DATA = {'': ['*.txt', '*.rst'], 'technical_indicators': ['*.txt'],
#            'technical_indicators.data': ['*.pkl']}

REQUIREMENTS_FILE = 'requirements.txt'
REQUIREMENTS = ''
if path.isfile(REQUIREMENTS_FILE):  # if file exists
    with open(REQUIREMENTS_FILE) as f:
        REQUIREMENTS = f.read()
        #REQUIREMENTS = f.read().splitlines()

# if not cleared they are added to bdist_egg root
if sys.argv[1] and str.lower(sys.argv[1]) != 'py2exe':
    DATA_FILES_PY2EXE = ''

setup(name=NAME,
      version=VERSION,
      description=DESC,
      long_description=LONG_DESC,
      license=LICENSE,
      url=URL,
      author=AUTHOR,
      author_email=EMAIL,

      keywords=KEYWORDS,
      classifiers=CLASSIFIERS,

      packages=find_packages(),
      #packages=find_packages(exclude=['tests*']),

      # only used if find_packages() does not work
      #packages=PACKAGES,
      #package_dir={'': NAME},

      # to create the Scripts exe using bdist_wininst build option
      entry_points=ENTRY_POINTS,

      install_requires=REQUIREMENTS,

      # used only if the package is not in PyPI, but exists as an egg,
      # sdist format or as a single .py file
      # see http://peak.telecommunity.com/DevCenter/setuptools#dependencies-that-aren-t-in-pypi
      #dependency_links = ['http://host.domain.local/dir/'],

      # required by bdist_egg and bdist_wheel
      include_package_data=True,
      package_data=PKG_DATA,

      zip_safe=False,

      # py2exe config
      #console=[SCRIPT],
      #data_files=DATA_FILES_PY2EXE,
      )
