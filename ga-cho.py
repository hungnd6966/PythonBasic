# -*- coding: utf-8 -*-
"""
Created on Sun Aug 16 21:29:03 2020

@author: hungnd
"""

## Viết chương trình để giải 1 câu đố cổ của Trung Quốc: Một trang trại thỏ và gà có 36
## đầu, 100 chân, hỏi số thỏ và gà là bao nhiêu?
def giai(con,chan):
    klg='Không có dáp án phù hợp!'
    for i in range(con+1):
        j=con-i
        if 2*i+4*j==chan:
            return i,j
    return klg,klg
con=36
chan=100
dap_an=giai(con,chan)
print (dap_an)