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
f=open("1213.in","r")

MI = lambda: map(int, f.readline().split())
LI = lambda: list(map(int, f.readline().split()))
II = lambda: int(f.readline())
IR = lambda: f.readline().rstrip()
LIR = lambda: list(f.readline().rstrip())
LIRS = lambda: list(f.readline().rstrip().split())
INF = math.inf

ans=0
idx=0
while True:
    IN=LIRS()
    if not IN:
        break
    ax=int(IN[2][2:-1])
    ay=int(IN[3][2:])
    IN=LIRS()
    bx=int(IN[2][2:-1])
    by=int(IN[3][2:])
    IN=LIRS()
    x,y=int(IN[1][2:-1]), int(IN[2][2:])
    IN=IR()
    x+=10000000000000
    y+=10000000000000
    sa=set([])
    cb,mb=divmod(x,bx)
    ca,ma=divmod(mb,ax)
    idx+=1
    while ma!=0 and ma not in sa and cb>=0:
        sa.add(ma)
        cb-=1
        mb+=bx
        ca,ma=divmod(mb,ax)
    if ma!=0 or cb<0:
        continue
    abx=math.lcm(ax,bx)
    abxa=abx//ax
    abxb=abx//bx
    warp=abxa*ay-abxb*by
    dist=y-(ca*ay+cb*by)
    if dist%warp==0 and dist//warp>=0:
        dw=dist//warp
        ca+=dw*abxa
        cb-=dw*abxb
        ans+=3*ca+cb
print(ans)
f.close()