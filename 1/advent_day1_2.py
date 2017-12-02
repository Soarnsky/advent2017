#!/usr/bin/python

import sys

with open("input.txt", "r") as f:
    captcha = f.read()
sum_captcha = 0
match_dist = len(captcha)/2

for idx, val in enumerate(captcha):
    next_idx = (idx + match_dist) % len(captcha)
    next_val = captcha[next_idx]

    if (val == next_val):
        sum_captcha = sum_captcha + int(next_val)
    
print sum_captcha

