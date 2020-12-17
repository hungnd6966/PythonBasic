# -*- coding: utf-8 -*-
"""
Created on Tue Aug  4 09:53:28 2020

@author: hungnd
"""

# Function for nth fibonacci number - Space Optimisataion 
# Taking 1st two fibonacci numbers as 0 and 1 
  
FibArray = [0,1] 
  
def fibonacci(n): 
    if n<0: 
        print("Incorrect input") 
    elif n<=len(FibArray): 
        return FibArray[n-1] 
    else: 
        temp_fib = fibonacci(n-1)+fibonacci(n-2) 
        FibArray.append(temp_fib) 
        return temp_fib 
  
# Driver Program 

def main():    
    n = int(input("Nhap so n= "))  
    print("Fibonaci of ", n, "is:",fibonacci(n)) 
if __name__ =="__main__":
    main()
#This code is contributed by Saket Modi 