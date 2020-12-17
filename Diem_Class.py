# -*- coding: utf-8 -*-
"""
Created on Sun Nov 22 08:48:25 2020

@author: hungnd
"""
from math import *

class Diem:
    # x
    # y 
    def __init__(self, x_0, y_0):
        self.x = x_0
        self.y = y_0
       
   
    def Datoado(self, x_moi, y_moi):
        self.x = x_moi
        self.y = y_moi

    def Khoangcach_Toigoctoado(self, x, y):
        return sqrt(self.x * self.x + self.y * self.y)

    def Dichchuyen(self, other):
        dx = self.x - other.x
        dy = self.y - other.y
        return sqrt(dx * dx + dy * dy)
    
    def Khoangcach_Haidiem(p1, p2):
        return sqrt((p1.x - p2.x)*(p1.x - p2.x) + (p1.y - p2.y)*(p1.y - p2.y))

if __name__ == "__main__":
    p0 = Diem(0,0)
    print("Diem khoi tao dau tien:",p0.x, p0.y)
    p1 = Diem(3, 4)
    print("Diem khoi tao dau tien:",p1.x, p1.y)  
    print("Khoag cach tu goc toa do toi p1:", p1.Khoangcach_Toigoctoado(3, 4))
    p3 = Diem(0,3)
    p4 = Diem(4,0)
    # kc = Khoangcach_Haidiem(p3, p4)
    print("khoang cach giua P3 vaf p4 la:", Diem.Khoangcach_Haidiem(p3, p4))
     # print(Diem.KhoangcahHaidiem(1, 5))

