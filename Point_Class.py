# -*- coding: utf-8 -*-
"""
Created on Sun Nov 22 08:48:25 2020

@author: hungnd
"""
from math import *
class Point:
    # x = 0
    # y = 0
    # def __init__(self):
    #     self.x = 0
    #     self.y = 0
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def set_location(self, x, y):
        self.x = x
        self.y = y
    def distance_from_origin(self):
        return sqrt(self.x * self.x + self.y * self.y)

    def distance(self, other):
        dx = self.x - other.x
        dy = self.y - other.y
        return sqrt(dx * dx + dy * dy) 
    def __str__(self):
        return "(" + str(self.x) + ", " + str(self.y) + ")"

if __name__ == "__main__":
    p0 = Point(0,0)
    print("Diem khoi tao P0:", p0.__str__())
    p = Point(3,4)
    print("Diem khoi tao ban dau p:", p.__str__())
    p1 = Point(5,5)
    print("Diem cos toa do moi p1:", p1.__str__())
    p2 = Point(4,4)
    print("Diem cos toa do moi p2:", p2.__str__())
    p1.set_location(0,3)
    print("Diem cos toa do moi p1:", p1.__str__())
    p2.set_location(4,0)
    print("Diem cos toa do moi p1:", p2.__str__())
    print("Khoan cach tu P1 toi p2:", p2.distance(p1))