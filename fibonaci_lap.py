# -*- coding: utf-8 -*-
#from __future__ import print_function 
"""
Created on Thu Aug 20 01:50:38 2020

@author: hungnd
"""

''' Module fib.py ''' 

import math
import os

def nhap():
    diem = float(input("Nhap diem cua Sinh vien:"))
    return diem
def kiemtra(diem):
    if diem >= 8.5 and diem < 10:
        print("Sinh vien xep loai: A")
    elif diem >= 7 and diem < 8.5:  
        print("Sinh vien xep loai: B")
    elif diem >= 6.5 and diem < 7:  
        print("Sinh vien xep loai: C")
    elif diem >= 5 and diem < 6.5:  
        print("Sinh vien xep loai: D")
    else:  
        print("Sinh vien xep loai: F")
        
def main():
    diem = nhap()
    kiemtra(diem)
    
if __name__ == '__main__':
    main()        