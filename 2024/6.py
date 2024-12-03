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
f=open("1203.in","r")

MI = lambda: map(int, f.readline().split())
LI = lambda: list(map(int, f.readline().split()))
II = lambda: int(f.readline())
IR = lambda: f.readline().rstrip()
LIR = lambda: list(f.readline().rstrip())
LIRS = lambda: list(f.readline().rstrip().split())
INF = math.inf
# sys.setrecursionlimit(3*(10**5))
# getcontext().prec=100

ans=0
enable=True
while True:
    try:
        flag=0
        flag2=0
        x,y=0,0
        IN=IR()
        if not IN:
            break
        for c in IN:
            if c=='m':
                flag=1
                x,y=0,0
            elif c=='u' and flag==1:
                flag=2
            elif c=='l' and flag==2:
                flag=3
            elif c=='(' and flag==3:
                flag=4
            elif c.isdigit() and flag==4:
                x=int(c)
                flag=5
            elif c.isdigit() and flag==5:
                x*=10
                x+=int(c)
            elif c==',' and flag==5:
                flag=6
            elif c.isdigit() and flag==6:
                y=int(c)
                flag=7
            elif c.isdigit() and flag==7:
                y*=10
                y+=int(c)
            elif c==')' and flag==7:
                flag=0
                flag2=0
                if enable:
                    ans+=x*y
                x,y=0,0
            else:
                flag=0
                x,y=0,0
            if flag!=0:
                flag2=0
            else:
                if c=='d':
                    flag2=1
                elif c=='o' and flag2==1:
                    flag2=2
                elif c=='(' and flag2==2:
                    flag2=3
                elif c==')' and flag2==3:
                    flag2=0
                    enable=True
                elif c=='n' and flag2==2:
                    flag2=4
                elif c=='\'' and flag2==4:
                    flag2=5
                elif c=='t' and flag2==5:
                    flag2=6
                elif c=='(' and flag2==6:
                    flag2=7
                elif c==')' and flag2==7:
                    flag2=0
                    enable=False
                else:
                    flag2=0
    except:
        break
print(ans)
f.close()