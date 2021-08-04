# -*- coding: utf-8 -*-
"""
Created on Fri Jul  2 13:43:23 2021

@author: BHUVI
"""

def attempt_float(x):
 try:return float(x)
 except:
  return x
print(attempt_float('1.2345'))