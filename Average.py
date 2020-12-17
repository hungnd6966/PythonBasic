# -*- coding: utf-8 -*-
"""
Created on Sun Aug 16 21:13:31 2020

@author: hungnd
"""
from __future__ import division, print_function, unicode_literals
def aver(n):
    sum=0
    for i in range(n):
        x=int(input("Nhập từng phần tử cần tính trung bình ="))
        sum = sum + x
    return sum/n

def main():
    n=int(input("Nhập s phần cần tính n="))
    print("Giá trị trung bình của các số vữa nhập:",aver(n))

if __name__ == '__main__':
    main()    