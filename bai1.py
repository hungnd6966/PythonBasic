# -*- coding: utf-8 -*-
"""
Created on Fri Nov 27 23:47:10 2020

@author: hungnd
"""

a=float(input("Chieu dai:"))
b=float(input("Chieu rong:"))
class Hinhchunhat:
    def __init__(self, chieudai, chieurong):
        self.chieudai=chieudai
        self.chieurong=chieurong
        def thongtin(self):
# setattr(hinh1, "chieudai", a)
# setattr(hinh1, "chieurong", b)
    print(getattr(hinh1, "chieudai"))
    print(getattr(hinh1, "chieurong"))
def chuvidientich(self):
print("Chu vi:", (self.chieudai+self.chieurong)*2)
print("Dientich", self.chieudai*self.chieurong)
def to_string(self):
ChieudaiH1 = str(self.chieudai)
ChieurongH1 =str(self.chieurong)
ChuviH1= str((self.chieudai+self.chieurong)*2)
DientichH1=str(self.chieudai*self.chieurong)
def luutru(self):
Kichco= 'Chieu dai:'+ str(self.chieudai)
Kichco+='\n' +'Chieu rong'+ str(self.chieurong)
Kichco+='\n'+'Chu vi:' + str((self.chieudai+self.chieurong)*2)
Kichco+='\n''Dien tich:'+ str(self.chieudai*self.chieurong)
a= open('hcn.txt', 'w+')
a.write(Kichco)
hinh1= Hinhchunhat(a,b)
hinh1.thongtin()
hinh1.chuvidientich()
hinh1.to_string()
hinh1.luutru()