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
f=open("1217.in","r")

MI = lambda: map(int, f.readline().split())
LI = lambda: list(map(int, f.readline().split()))
II = lambda: int(f.readline())
IR = lambda: f.readline().rstrip()
LIR = lambda: list(f.readline().rstrip())
LIRS = lambda: list(f.readline().rstrip().split())
INF = math.inf

a=int(LIRS()[2])
b=int(LIRS()[2])
c=int(LIRS()[2])
IR()
IN=list(map(int,LIRS()[1].split(',')))
print(a,b,c,IN)
ptr=0
out=[]
while ptr<len(IN):
    opcode,operand=IN[ptr],IN[ptr+1]
    if operand==4:
        combo=a
    elif operand==5:
        combo=b
    elif operand==6:
        combo=c
    else:
        combo=operand
        
    if opcode==0:
        a=(a//(2**combo))
    elif opcode==1:
        b=b^operand
    elif opcode==2:
        b=combo%8
    elif opcode==3:
        if a!=0:
            ptr=operand
            continue
    elif opcode==4:
        b=b^c
    elif opcode==5:
        out.append(combo%8)
    elif opcode==6:
        b=(a//(2**combo))
    elif opcode==7:
        c=(a//(2**combo))
    ptr+=2
print(*out,sep=',')
f.close()