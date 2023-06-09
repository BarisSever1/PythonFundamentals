import math
import os
import random
import re
import sys


def flatland():
    n = 6
    c = [0, 1, 3, 4, 5, 2]
    ct = 0
    city_list = []
    for i in range(n):
        city_list.append(i)
        ct += 1
    all_dist = []
    for x in city_list:
        distance = []
        for s in c:
            distance.append(abs(s - x))
        all_dist.append(min(distance))

    return max(all_dist)


print(flatland())
