import sys
import math
abc, row, row00 = "ABCDEFGHIJKLMNOPQRSTUVWXYZ?", [], [[], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], []]
l = int(input())
h = int(input())
t = input()
for i in range(h):
    row += [input()]

for letter in t:
    index = 1000
    count = 0
    for r in row:
        for which in abc:
            if letter.upper() == which:
                if l > 5:
                    index = abc.index(which) * 20
                else:
                    index = abc.index(which) * 4
        if index == 1000:
            if l > 5:
                index = abc.index("?") * 20
            else:
                index = abc.index("?") * 4
        if l > 5:
            row00[count] += (r[index:index + 20])
            count += 1
        else:
            row00[count] += (r[index:index + 4])
            count += 1


for x in range(h):
    print(''.join(row00[x]))






