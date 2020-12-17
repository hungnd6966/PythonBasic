# -*- coding: utf-8 -*-
"""
Created on Tue Aug  4 08:49:08 2020

@author: hungnd
"""

# Function for nth Fibonacci number 
  
def Fibonaci(n): 
    if n<0: 
        print("Incorrect input") 
    # First Fibonacci number is 0 
    elif n==1: 
        return 0
    # Second Fibonacci number is 1 
    elif n==2: 
        return 1
    else: 
        return Fibonaci(n-1)+Fibonaci(n-2) 
  
# Driver Program 
n = int(input("Nhap so n tu ban phim:"))
print("Fibonaci cuar",n, " la: ",Fibonaci(n)) 
  
