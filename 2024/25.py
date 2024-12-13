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
    #print(ax,ay,bx,by,x,y)
    cnt=INF
    ca=x//ax
    mx=ca*ax
    cb=(x-mx)//bx
    mx+=cb*bx
    my=ca*ay+cb*by
    
    while ca>=0:
        if mx==x and my==y:
            cnt=min(cnt,3*ca+cb)
            #print(x,mx,ax,bx,ca,cb,cnt)
        ca-=1
        mx=ca*ax
        cb=(x-mx)//bx
        mx+=cb*bx
        my=ca*ay+cb*by
    if cnt!=INF:
        ans+=cnt
    IN=IR()
print(ans)
f.close()