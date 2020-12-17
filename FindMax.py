# -*- coding: utf-8 -*-
"""
Created on Tue Aug  4 10:31:53 2020

@author: hungnd
"""

def find_max(nums):
    max = nums[0]
    for x in nums:
      if x > max:
        max = x
    print("max value:",max)

def main():
  find_max([2, 4, 9, 7, 19, 94, 5])

if __name__ == '__main__':
  main()