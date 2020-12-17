# -*- coding: utf-8 -*-
"""
Created on Fri Aug  2 21:41:05 2019

@author: hungnd
"""
# -*- coding: utf-8 -*-  # Sử dụng utf-8
#coding:utf-8
#Program by hungnd
from __future__ import division, print_function, unicode_literals
import math # tai cacs thu vien

def giai_pt(a,b,c):
    delta = b*b - 4*a*c
    if delta > 0 :
        x1 = (-b + math.sqrt(delta))/(2*a)
        x2 = (-b - math.sqrt(delta))/(2*a)
        print("phuong trinh bac 2 co hai nghiem phan biet")
        print("x1= %3.2f x2= %3.2f " %(x1,x2))
    elif delta ==0 :
       print("phuong trinh co nghiem kep x1=x2= %3.2f" %(-b/2*a))
    else :
       print("phuong trinh vo nghiem")
def main():
    print("Nhap lan luot he so a,b,c cua phuong trinh bac 2")
    a = float(input('he so a:'))
    b = float(input('he so b:'))
    c = float(input('he so c:'))
    giai_pt(a,b,c)
if __name__ == '__main__':
  main()