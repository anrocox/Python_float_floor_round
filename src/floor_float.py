#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
Created on Jul 16, 2014

@author: anroco

In Python how approximate a float to the nearest integer below?

En Python, ¿Cómo aproximar un float a entero más cercano por abajo?
'''

import math

#create a float number
f = 23.123
print(f)

#return floor of f, rounded to the nearest integer toward negative infinity
f_aprox = math.floor(f)
print(f_aprox)

#create a float number
f = 39.999
print(f)

#approaches always made down
f_aprox = math.floor(f)
print(f_aprox)
