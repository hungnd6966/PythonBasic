# -*- coding: utf-8 -*-
"""
Created on Tue Aug  4 10:42:39 2020

@author: hungnd
"""

def count_to_n(n):
    for i in range(1, n + 1):
        print('*', end=' ')
print()

def main():
    for i in range(1, 10):
        count_to_n(i)
        print()
if __name__ == '__main__':
  main()    