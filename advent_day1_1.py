#!/usr/bin/python

import sys

args = sys.argv[1:]
captcha = args[0]
sum_captcha = 0

for idx, val in enumerate(captcha):
    
    if (idx+1 < len(captcha)):
        next_val = captcha[idx+1]
   
    if (idx == len(captcha)-1):
        next_val = captcha[0]

    if (val == next_val):
        sum_captcha = sum_captcha + int(next_val)
    
print sum_captcha

