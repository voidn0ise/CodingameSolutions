import sys
import math
import re

n, q = int(input()), int(input())
final = {}

for i in range(n):
    ext = input()
    final[(ext.split()[0]).lower()] = (ext.split()[1])

for x in range(q):
    file = input()
    found = re.search(r'(\.)([a-zA-Z0-9]{1,10}$)', file, re.IGNORECASE)
    if file == "...":
        print("UNKNOWN")
    elif found:
        try:
            print(final[found.group(2).lower()])
        except KeyError:
            print("UNKNOWN")
    else:
        print("UNKNOWN")










