#!/usr/bin/python


import random

def genknuth(m,n):
    """USAGE: genknuth(int m,int n) """
    for i in xrange(n):
        if (random.getrandbits(128)%(n-i)) < m:
            print i
            m -= 1

genknuth(10,100)
