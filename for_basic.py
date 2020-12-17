# -*- coding: utf-8 -*-
"""
Created on Tue Aug  4 10:42:39 2020

@author: hungnd
"""

def count_to_n(n):
    for i in range(1, n + 1):
        print('*', end=' ')
        print()

    
def hello():
        for i in range(0,2): 
                print("hello world")
                print("Nguyen Duong Hung")
                print("Hoc vien Ngan hang")
        for j in range(0,20):
                if j % 5 == 0:
                        print(j)
def main():
    hello()
    count_to_n(10)
    
if __name__ == '__main__':
  main()    