import sys
import math
import re

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

n = int(input())  # the number of temperatures to analyse
temps = input()  # the n temperatures expressed as integers ranging from -273 to 5526

# Write an action using print
# To debug: print("Debug messages...", file=sys.stderr)

if n > 0:
    printed = True
    num2 = 0
    nums = (temps.split(" "))
    nums = list(map(int, nums))
    for num in nums:
        if num + (min(nums, key=abs)) == 0:
            print(str(min(nums, key=abs)).strip("-"))
            printed = False

    if printed:
        print(min(nums, key=abs))
else:
    print(n)
