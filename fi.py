# -*- coding: utf-8 -*-
#from __future__ import print_function 
"""
Created on Thu Aug 20 01:50:38 2020

@author: hungnd
"""

''' Module fib.py ''' 


def even_fib(n): 
    total = 0 
    f1, f2 = 1, 2 
    while f1 < n: 
        if f1 % 2 == 0: 
            total = total + f1 
        f1, f2 = f2, f1 + f2 
    return total 

if __name__ == "__main__": 
    limit = int(input("Max Fibonacci number: ")) 
    for i in range(1,limit):   
        print(even_fib(i)) 
