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
INF = math.inf

IN=[2,4,1,3,7,5,4,0,1,3,0,3,5,5,3,0]
def fun(a):
    b=0
    c=0
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
    return out
ans=1
flag=True
ln=1
cnt=0
while flag:
    if fun(ans)==IN[-ln:]:
        if ln==len(IN):
            flag=False
        else:
            ln+=1
            ans*=8
    else:
        cnt+=1
        ans+=1
        if cnt==8:
            cnt=0
            ans//=8
            ln-=1
print(ans)