# -*- coding: utf-8 -*-
"""
Created on Fri Jul  2 13:02:03 2021

@author: BHUVI
"""

import numpy as np
strings = ['foo', 'card', 'bar', 'aaaa', 'abab']
strings.sort(key=lambda x: len(set(list(x))))
print(strings)