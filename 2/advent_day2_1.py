#!/usr/bin/python

import sys

with open("input.txt", "r") as f:
    spreadsheet = f.readlines()

spreadsheet = [x.strip() for x in spreadsheet]
sum = 0
for row in spreadsheet:
    numbers = row.split()
    lowest = highest = int(numbers[0])
    for num in numbers:
        val = int(num)
        if val > highest:
            highest = val
        if val < lowest:
            lowest = val
    difference = highest - lowest
    sum = sum + difference
print sum
     

