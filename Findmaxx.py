# -*- coding: utf-8 -*-
"""
Created on Thu Aug 20 11:05:12 2020

@author: hungnd
"""

def find_max(nums):
    max = nums[0]
    for x in nums:
      if x > max:
        max = x
    print("max value:",max)

def main():
  #  find_max([2, 4, 9, 7, 19, 94, 5])
    data = []
    n = int(input('Enter how many elements you want: '))
    for i in range(0, n):
        x = input('Enter the numbers into the array: ')
        data.append(x)
    print(data)
    find_max(data)

if __name__ == '__main__':
  main()