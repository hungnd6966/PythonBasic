# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

#import math

def fractorial(n):
    if n == 0 :
        return 1 
    else:
        return fractorial(n-1)*n

## main 
def sum(n):
    s = 0
    for i in range(n):
        s = s + 1/fractorial(i)
    return s    

def main():
    print("Chuong trinh tinh gia thua")  
    n = int(input("Nhap so n de tinh giai thua n = "))
    print("Giai thua cua n:", fractorial(n))      
    print("Factorail of ",n , " is : ",fractorial(n))
    print("Sum  of ",n , " is : ",sum(n))
 
if __name__ == "__main__":
    main()    