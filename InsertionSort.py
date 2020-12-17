# -*- coding: utf-8 -*-
"""
Created on Sun Aug 16 21:27:23 2020

@author: hungnd
"""

def insort(a):

    for i in range(1, len(a)):

        b=a[i]

        j=i-1

        while j>=0 and b<a[j]:

            a[j],a[j+1]=a[j+1],a[j]

            j -= 1

a = [ 80,20,5, 6, 4, 1,3,2, 100]

insort(a)

for i in a:

    print (i)