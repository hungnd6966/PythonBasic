# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

#Khoi tao mot mang rong de chua phan tu

alist = [] 
def _input():
    n = int(input("Nhap so phan tur cua day : "))  
    for i in range(0, n): 
        ele = int(input()) 
        alist.append(ele) # adding the element 
#    return alist  
    #print("Day nhap vao",alist) 

#_input()    
def _print():
    for i in range(len(alist)):
        print("Phan tu thu:",alist[i])
        
def shortBubbleSort(alist):
    exchanges = True
    passnum = len(alist)-1
    while passnum > 0 and exchanges:
       exchanges = False
       for i in range(passnum):
           if alist[i]>alist[i+1]:
               exchanges = True
               temp = alist[i]
               alist[i] = alist[i+1]
               alist[i+1] = temp
       passnum = passnum-1
       
def _min(alist):
    min = alist[0]
    exchanges = True
    passnum = len(alist)-1
    while passnum > 0 and exchanges:
       exchanges = False
       for i in range(passnum):
           if alist[i] < min:             
               min = alist[i]
       passnum = passnum-1     
    return min  

def _max(alist):
    max = alist[0]
    exchanges = True
    passnum = len(alist)-1
    while passnum > 0 and exchanges:
       exchanges = False
       for i in range(passnum):
           if alist[i] > max:             
               max = alist[i]
       passnum = passnum-1     
    return max 
#alist=[20,30,40,90,50,60,70,80,100,110]
if __name__ == "__main__":    
    
    # _input()
    alist=[200,20,30,40,2000,90,10,1000,50,60,70,10,5,80,100,2,110]
    print("Gia tri nho nhat cua day:", _min(alist))
    print("Gia tri lon nhat cua day:", _max(alist))
    # _print()
    shortBubbleSort(alist)
    # _print()
    print("Day da sap xep",alist)
    