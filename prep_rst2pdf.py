#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Remove parts of rST to create a better pdf.
"""

# Python 3 compatibility
from __future__ import (absolute_import, division, print_function,
                        unicode_literals)


with open('doc/index.ori') as f:
    text = f.readlines()

new_text = ''

for line in text:
    if 'Contents:' in line:
        pass
    elif 'Indices and tables' in line:
        break
    else:
        new_text += line

with open('doc/index.rst', 'w') as f:
    f.writelines(new_text)
