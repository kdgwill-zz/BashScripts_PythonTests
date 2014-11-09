#!/usr/bin/python

cache = {}

def fib(n) :
    if n in cache.keys() : return cache[n];
    temp = 0;
    if n==0:temp=0
    elif n<3 : temp =  1;
    else : temp = fib(n-1) + fib(n-2)
    cache[n]=temp
    return temp;

print "Begining"
for i in xrange(0,100,1):
    print fib(i)
print "Completed"

