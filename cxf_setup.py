#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Setup for cx_Freeze"""

# Python 3 compatibility
from __future__ import (absolute_import, division, print_function,
                        unicode_literals)
import sys
from cx_Freeze import setup, Executable
from technical_indicators import (NAME, VERSION, DESC, LONG_DESC, LICENSE, URL,
                                  AUTHOR, EMAIL, KEYWORDS, CLASSIFIERS, SCRIPT,
                                  DATA_FILES_CXF)


TARGET_NAME = NAME + '.exe'

base = None
# GUI applications require a different base on Windows
if sys.platform == 'win32':
    base = 'Win32GUI'

##if 'bdist_msi' in sys.argv:
##    sys.argv += ['--install-script', 'install.py']

##bdist_msi_options = {
##    'initial_target_dir': r'[ProgramFilesFolder]\%s\%s' % (AUTHOR, NAME),
##    #'upgrade_code': '{66620F3A-DC3A-11E2-B341-002219E9B01E}',
##    #'add_to_path': False,
##    }

build_exe_options = dict(compressed=True,
                         #excludes=["macpath", "PyQt4"],
                         #includes=['atexit', 'PySide.QtNetwork'],
                         include_files=DATA_FILES_CXF,
                         # append any extra module by extending the list below
                         # - "contributed_modules+["lxml"]"
                         #packages=contributed_modules
                         )

setup(name=NAME,
      version=VERSION,
      description=DESC,
      long_description=LONG_DESC,
      license=LICENSE,
      url=URL,
      author=AUTHOR,
      author_email=EMAIL,

      classifiers=CLASSIFIERS,
      platform='any',
      keywords=KEYWORDS,

      executables=[Executable(script=SCRIPT,
                              base=base,
                              compress=True,
                              #icon="app_name.ico",
                              targetName=TARGET_NAME,
                              #copyDependentFiles=True
                              )],

      options=dict(build_exe=build_exe_options),
      ##options=dict(bdist_msi=bdist_msi_options,
      ##             build_exe=build_exe_options),
      ##scripts=['install.py']
      )
