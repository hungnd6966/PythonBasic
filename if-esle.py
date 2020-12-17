# -*- coding: utf-8 -*-
#from __future__ import print_function 
"""
Created on Thu Aug 20 01:50:38 2020

@author: hungnd
"""

''' Module fib.py ''' 

import math

def nhap():
    diem = float(input("Nhap diem cua sinh vien:"))
    return diem

def kiemtra(diem):
    if diem >= 8.5 and diem <= 10:
        print("Sinh viên đạt loại A")
    elif diem >= 7.0 and diem < 8.5:
        print("Sinh viên đạt loại B")   
    elif diem >= 5.0 and diem < 7:
        print("Sinh viên đạt loại C")   
    elif diem >= 3.0 and diem < 5:
        print("Sinh viên đạt loại D")
    else:    
        print("Sinh viên đạt loại F")
        
def main(): 
    diem_SV = nhap()
    kiemtra(diem_SV)
    
if  __name__ == '__main__':
    print("Chuong trinh chuyen doi diem chosinh vien")
    main()