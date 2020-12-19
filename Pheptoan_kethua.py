# -*- coding: utf-8 -*-
"""
Created on Fri Nov 27 14:12:08 2020

@author: hungnd
"""

class Calculation1:
    def Summation(self, a, b):
        return a + b
class Calculation2:
    def Multiplication(self, a, b):
        return a * b;
class Derived(Calculation1, Calculation2):
    def Divide(self, a, b):
        return a / b
d = Derived()
print("a + b = ",d.Summation(10, 20))
print("a * b = ", d.Multiplication(10, 20))
print("a / b = ", d.Divide(10, 20))
