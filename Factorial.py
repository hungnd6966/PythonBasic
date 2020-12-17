# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

from math import *

def giaithua(n):
    if n == 0 :
        return 1 
    else:
        return giaithua(n-1)*n

## main 
def main():
    print("Chuong trinh tinh gia thua")  
    n = int(input("Nhap so n de tinh giai thua n = "))
    print("Giai thua cuar n:", giaithua(n))  
if __name__ == '__main__':
    main()
     