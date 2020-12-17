# -*- coding: utf-8 -*-
"""
Created on Wed Aug  5 19:50:25 2020

@author: hungnd
"""
def FahToCel():
    Fahrenheit = int(input("Enter a temperature in Fahrenheit: "))
    
    Celsius = (Fahrenheit - 32) * 5.0/9.0
    
    print("Temperature:", Fahrenheit, "Fahrenheit = ", Celsius, " C")



def CelToFah():
    Celsius = int(input("Enter a temperature in Celsius: "))
    
    Fahrenheit = 9.0/5.0 * Celsius + 32
    
    print("Temperature:", Celsius, "Celsius = ", Fahrenheit, " F")
def main():
    FahToCel()    
    CelToFah()
if __name__ == '__main__':
    main()    