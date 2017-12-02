#!/usr/bin/python

import sys

with open("input.txt", "r") as f:
    spreadsheet = f.readlines()

spreadsheet = [x.strip() for x in spreadsheet]
sum = 0
for row in spreadsheet:
    numbers = row.split()
    for num in numbers:
        val = int(num)
        for i in range(0, len(numbers)):
            check_num = int(numbers[i])
            if val != check_num and val < check_num:
                if check_num % val == 0:
                    solution = check_num/val
    sum = sum + solution
print sum
     

