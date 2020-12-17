# -*- coding: utf-8 -*-
"""
Created on Fri Sep 11 15:37:49 2020

@author: hungnd
"""

# i = 10 
# arr = []
# while i > 0:
#     arr.append(i)
#     print(i)
#     i = i - 1
# print(arr)


# n = 10 
# arr = []
# for i in range(5,n-1):
#     arr.append(i)
#     print(i)
#     i = i - 1
# print(arr)

# diem = float(input("Nhap diem tong ket:"))
# if diem >=8.5: print('A')
# elif diem >= 7.5 and diem < 8.5: print("B")  
# elif diem >= 6.0 and diem < 7.5: print("C")
# elif diem >= 4.5 and diem < 6.0: print("D")
# else: print("F") 


n = 1
arr = []
while n <= 100:
    if n % 2 == 0: arr.append(n)
    n = n + 1
print(arr) 
