#!/usr/bin/env python
import math

inputnum = int(input().strip())
output = ""
for num in range(inputnum):
    result = []
    root1=0
    root2=0
    root1_str=""
    root2_str=""
    inputlist = input().split()
    inputlist = [int(i) for i in inputlist]
    A = inputlist[0]
    B = inputlist[1]
    C = inputlist[2]
    discriminant = (B ** 2 - (4 * A * C))
    discrim_sqrt = math.sqrt(abs(discriminant))
    if discriminant > 0:
        # real roots
        root1 = int((-B + discrim_sqrt) / (2 * A))
        root2 = int((-B - discrim_sqrt) / (2 * A))
    elif discriminant == 0:
        # equal and real roots
        root1 = int(-B / (2 * A))
        root2 = int(-B / (2 * A))
    elif discriminant < 0:
        # complex roots
        root1 = int(-B / (2 * A))
        root2 = int(-B / 2 * A)

    if discriminant < 0:
        root1_str = str(root1) + "+{}i".format(int(discrim_sqrt))
        root2_str = str(root2) + "-{}i".format(int((discrim_sqrt)))
    else:
        root1_str = str(root1)
        root2_str = str(root2)

    if root1 >= root2:
        output += "{} {}".format(root1_str,root2_str) + "; "
    else:
        output += "{} {}".format(root2_str, root1_str) + "; "

print(output.strip("; "))
