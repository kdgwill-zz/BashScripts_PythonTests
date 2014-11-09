#!/usr/bin/python
import math
import time
import random
import Sort #local

list1 = []
for i in range(0,1000000):
    num = random.uniform(0,1000000)
    num = math.trunc(num)
    list1.append(num)
list2 = list1[:]#proper way to copy

ms = Sort.mergeSort();
qs = Sort.quickSort();

#print "Original List [", list1

print "Begining Merge Sort"
timeStamp = time.time();
ms.sort(list1);
timeStamp = time.time()-timeStamp
print "Merge Sort Concluded @ ",timeStamp," Seconds"

print "Begining Quick Sort"
timeStamp = time.time();
qs.sort(list2);
timeStamp = time.time()-timeStamp
print "Quick Sort Concluded @",timeStamp," Seconds"
"""
print "Mergesort List["
print list1
print "Quicksort List["
print list2
"""
