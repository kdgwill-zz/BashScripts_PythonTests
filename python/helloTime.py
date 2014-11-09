#!/usr/bin/python

import time;
import calendar;

localtime = time.localtime(time.time())
localtime = time.asctime(localtime)
print time.timezone
print "Local time:", localtime

cal  = calendar.month(2014,8)
cal2 = calendar.month(2014,9)
cal3 = calendar.month(2014,10)
print cal, cal2, cal3
