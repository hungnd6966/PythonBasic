# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

#Khoi tao mot mang rong de chua phan tu
alist = [] 
class bubblesort:
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
    #alist=[20,30,40,90,50,60,70,80,100,110]
if __name__ == "__main__":    
    
   bubblesort._input()
   bubblesort._print()
   bubblesort.shortBubbleSort(alist)
   bubblesort._print()
   print("Day da sap xep",alist)