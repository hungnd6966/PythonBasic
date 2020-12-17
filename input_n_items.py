# -*- coding: utf-8 -*-
"""
Created on Thu Aug 20 12:01:14 2020

@author: hungnd
"""

### -*- coding: utf-8 -*-
"""
Created on Thu Aug 20 11:05:12 2020

@author: hungnd
"""
data = []
n = 0
def Nhap(nums):
    n = int(input('Enter how many elements you want: '))   
    for i in range(0, n):
        x = input('Enter the numbers into the array: ')
        data.append(int(x))
    
def in_day(data):
    print(data)
 
def sort(data):
    data.sort()    
def main():
    Nhap(n)
    in_day(data)
    sort(data)
    in_day(data)
if __name__ == '__main__':
    main()
    