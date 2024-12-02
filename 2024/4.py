import sys, math
from collections import deque, defaultdict, Counter
from itertools import permutations, combinations, product
from bisect import bisect_left, bisect_right
from copy import deepcopy
from fractions import Fraction
from decimal import *
from heapq import heapify, heappop, heappush, heappushpop
from datetime import datetime
from functools import cache
input = sys.stdin.readline
f=open("1202.in","r")

MI = lambda: map(int, f.readline().split())
LI = lambda: list(map(int, f.readline().split()))
II = lambda: int(f.readline())
IR = lambda: f.readline().rstrip()
LIR = lambda: list(f.readline().rstrip())
LIRS = lambda: list(f.readline().rstrip().split())
INF = math.inf
# sys.setrecursionlimit(3*(10**5))
# getcontext().prec=100

def func(arr):
    x=arr[0]
    if arr[0]<arr[1]:
        flag=True
    elif arr[0]>arr[1]:
        flag=False
    else:
        return False
    for i in arr[1:]:
        if 1<=abs(x-i)<=3 and (i!=x) and flag^(x>i):
            x=i
            continue
        else:
            break
    else:
        return True
    return False

cnt=0
while True:
    try:
        IN=LI()
        if len(IN)<=2:
            break
        if func(IN):
            cnt+=1
        else:
            for i in range(len(IN)):
                if func(IN[:i]+IN[i+1:]):
                    cnt+=1
                    break
    except:
        break
print(cnt)
f.close()