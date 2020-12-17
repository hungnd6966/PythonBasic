# -*- coding: utf-8 -*-
"""
Created on Sun Nov 15 14:50:07 2020

@author: hungnd
"""
## Chuong trinh nhap mot day so nguyen tu ban phim

def nhap():
    try:
        raw_input          # Python 2
    except NameError:
        raw_input = input  # Python 3

    user_input = raw_input('Go cac so cach nhau boi dau phay:\n').strip()
    numList = [int(item) for item in user_input.split(',')]
  #  print(selection_sort(unsorted))
    return numList

if __name__ == "__main__":
    lt = nhap()
    print(lt)