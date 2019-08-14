#! /usr/bin/python
# -*- coding: UTF-8 -*-

#########################################################################
# File Name: bch_polynome.py
# Author: cosim
# mail: cosimzhou@hotmail.com
# Created Time: 六  8/10 15:39:51 2019
#########################################################################


from bchcode import BCHCoder as bch
from polynome import Polynome as poly

m1 = '10100110111'
m2 ='1111100100101'

def chk(a, b, n):
    a = poly(a)
    b = poly(b)
    d = b<<n
    c = d%a#+b
    return c.printf(binary=True)

b = bch(15, 5, m1)
b1= bch(18, 6, m2)

data = ('1001001101101010110', '1010101010101101', '0', '11111111111')

#a = poly('1100100101')
#b = poly(m1)
#m = poly('11011010')
#c = a*b+m
#print data[0], c.printf(binary=True)
#exit(0)
for d in data:
    print b.encode(d), chk(m1, d, 10)


