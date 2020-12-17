# -*- coding: utf-8 -*-
"""
Created on Tue Aug  4 09:53:28 2020

@author: hungnd
"""

# Function for nth fibonacci number - Space Optimisataion 
# Taking 1st two fibonacci numbers as 0 and 1 
  
def fibonacci(n): 
    a = 0
    b = 1
    if n < 0: 
        print("Incorrect input") 
    elif n == 0: 
        return a 
    elif n == 1: 
        return b 
    else: 
        for i in range(2,n): 
            c = a + b 
            a = b 
            b = c 
        return b 
  
# Driver Program 

def main():    
    n = int(input("Nhap so n= "))  
    print("Fibonaci of ", n, "is:",fibonacci(n)) 
if __name__ =="__main__":
    main()
#This code is contributed by Saket Modi 