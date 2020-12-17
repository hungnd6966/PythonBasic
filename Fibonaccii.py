# -*- coding: utf-8 -*-
"""
Created on Thu Aug 20 12:26:30 2020

@author: hungnd
"""

def fibo(n):
    if n == 0 or n == 1:
        return 1
    else:
        return fibo(n-1) + fibo(n-2)
def testfi(n):
    for i in range(n+1):
        print('fibonaci  of', i, '=',fibo(i))
def main():
    a = int(input('Nhap so can tinh:'))
    testfi(a)
#Chi dinh ham main lam viec
if __name__ == '__main__':
    main()