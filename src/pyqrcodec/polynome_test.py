#! /usr/bin/python
# -*- coding: utf-8 -*-
'''
Created on 2014年7月22日

@author: zhouzhichao
'''

from polynome import Polynome
import unittest

class TestPolynome(unittest.TestCase):
    def setUp(self):
        print "setUp TestPolynome test case."
    def tearDown(self):
        print "tearDown TestPolynome test case."
    def test_mul(self):
        p1, p2 = Polynome(value="1010110101011"), Polynome(value="1010101011")
        p = p1 * p2
        print p1.order, p2.order
        print p1.printf(), p2.printf(), p.printf()

    def test_mod(self):
        str1, str2 = "1010110101011", "1010101011"
        p1, p2 = Polynome(value=str1), Polynome(value=str2)
        p = p1 % p2
        q = p1 / p2

        s =q * p2 + p#11011010
        print "s:",s.printf()
        print "p1:",p1.printf()
        self.assertEqual(p2 % p1, p2)
        self.assertTrue(s== p1)
        print p1.order, p2.order
        print p1.printf(), p2.printf(), p.printf()

    def test_add(self):
        str1, str2 = "1010110101011", "1010101011"
        p1, p2 = Polynome(value=str1), Polynome(value=str2)
        p = p1 + p2
        print p1.order, p2.order, p.order
        self.assertEqual(p.order, len(str1))
        self.assertEqual((p1+p1).order, 0)
        print p1.printf(), p2.printf(), p.printf()

    def test_self_justifying(self):
        def single_test(sa, sb, sc):
            a, b, c = Polynome(sa), Polynome(sb), Polynome(sc)
            res = a * b + c
            oa, ob = res / b, res / a
            c1, c2 = res % a, res % b
            print a.printf(), b.printf(), c.printf(), res.printf()
            print oa.printf(), ob.printf(), c1.printf(), c2.printf()
            self.assertEqual(c, c1)
            self.assertEqual(c, c2)
            self.assertEqual(a, oa)
            self.assertEqual(b, ob)

        abarray = ('10101101011010001',
                   '1001000010000100',
                   '1111111111000000000',
                   '1000000000000000'
                   '11110000111100101',
                   '1111111111111111',
                   '1001001010000101',
                   '10010101110100011',
                   '1010101010101010',
                   '1000000101010101'
                )
        clist   = ('1010010',
                   '10100010110',
                   '111111',
                   '1',
                   '0',
                   '10000',
                   '1111111111'
                )

        for i, a in enumerate(abarray):
            for j, b in enumerate(abarray):
                for c in clist:
                    print i,j,c
                    single_test(a, b, c)


    def test_printf(self):
        value = "1010110101011"
        polynome = "x^12+x^10+x^8+x^7+x^5+x^3+x^1+x^0"

        p = Polynome(value=value)
        self.assertEqual(value, p.printf())
        self.assertEqual(value, p.printf(binary=True))
        self.assertEqual(polynome, p.printf(polynome=True))
        self.assertEqual(value, p.printf(polynome=True, binary=True))
        self.assertEqual(value[::-1], p.printf(binary=True, desc=True))
        self.assertEqual(value[::-1], p.printf(desc=True))
        self.assertEqual("+".join(polynome.split("+")[::-1]), p.printf(polynome=True, desc=True))

        p = Polynome(order=12)
        value = "0"*12
        polynome = "0"

        self.assertEqual(value, p.printf())
        self.assertEqual(value, p.printf(binary=True))
        self.assertEqual(polynome, p.printf(polynome=True))
        self.assertEqual(value, p.printf(polynome=True, binary=True))
        self.assertEqual(value[::-1], p.printf(binary=True, desc=True))
        self.assertEqual(value[::-1], p.printf(desc=True))
        self.assertEqual("+".join(polynome.split("+")[::-1]), p.printf(polynome=True, desc=True))

if __name__ == '__main__':
    unittest.main()
