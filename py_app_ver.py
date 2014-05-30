#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Write Python and application version (from ChangeLog.rst) to text files.
"""

# Python 3 compatibility
from __future__ import (absolute_import, division, print_function,
                        unicode_literals)
import sys


py_ver = sys.version.split()[0]
py_ver = py_ver.split('.')
py_ver = str(py_ver[0] + '.' + py_ver[1])

with open('ChangeLog.rst') as f:
    app_ver = f.readline().split()[0]

with open('py_ver.txt', 'w') as f:
    f.write(py_ver)

with open('app_ver.txt', 'w') as f:
    f.write(app_ver)
