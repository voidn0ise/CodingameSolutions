import sys
import math
import re

n, q, ftype, mime = int(input()), int(input()), [], []

for i in range(n):
    ext = input()
    ftype += [ext.split(" ")[0]]
    mime += [ext.split(" ")[1]]

for x in range(q):
    file = input()
    res = re.search(r'(^.*)(\.\w+$)', file)
    if res.group(2).strip(".") in ftype:
        print(mime[ftype.index(res.group(2).strip("."))])
    else:
        print("UNKNOWN")









