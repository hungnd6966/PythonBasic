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

    user_input = raw_input('Enter numbers separated by a comma:\n').strip()
    numList = [int(item) for item in user_input.split(',')]
  #  print(selection_sort(unsorted))
    return numList

def listsum(numList):
    if len(numList) == 1:
        return numList[0]
    else:
        return numList[0] + listsum(numList[1:])

# def main():
#     numList = nhap()
#     print("Tong cua day:", listsum(numList))
  #  print(listsum([1,3,5,7,9,11]))
    #Chi dinh ham main() lam viec
# if __name__ == '__main__':
    # main()
if __name__ == '__main__':
    # main()
    numList = nhap()
    print("Tong cua day:", listsum(numList))