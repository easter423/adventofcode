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
f=open("1206.in","r")

MI = lambda: map(int, f.readline().split())
LI = lambda: list(map(int, f.readline().split()))
II = lambda: int(f.readline())
IR = lambda: f.readline().rstrip()
LIR = lambda: list(f.readline().rstrip())
LIRS = lambda: list(f.readline().rstrip().split())
INF = math.inf

board=[]
x,y=0,0
flag=True
while True:
    IN=LIR()
    if IN:
        board.append(IN)
        if flag and '^' in IN:
            y=IN.index('^')
            flag=False
        elif flag:
            x+=1
    else:
        break
bx,by=len(board),len(board[0])
dx=[-1,0,1,0]
dy=[0,1,0,-1]
didx=0
cnt=1
board[x][y]='X'
while True:
    nx,ny=x+dx[didx],y+dy[didx]
    if nx<0 or nx>=bx or ny<0 or ny>=by:
        break
    elif board[nx][ny]=='#':
        didx+=1
        didx%=4
    else:
        if board[nx][ny]=='.':
            cnt+=1
            board[nx][ny]='X'
        x,y=nx,ny
print(cnt)
f.close()