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
board[x][y]='X'
ans=set([])

def fun(x,y,didx):
    global ans
    b=deepcopy(board)
    nx,ny=x+dx[didx],y+dy[didx]
    b[nx][ny]='#'
    didx+=1
    didx%=4
    cnt=0
    while True:
        nx,ny=x+dx[didx],y+dy[didx]
        if nx<0 or nx>=bx or ny<0 or ny>=by:
            return False
        elif b[nx][ny]=='#':
            didx+=1
            didx%=4
        else:
            if b[nx][ny]=='.':
                b[nx][ny]='X'
                cnt=0
            x,y=nx,ny
        cnt+=1
        if cnt>1000:
            return True
done=set([])
while True:
    nx,ny=x+dx[didx],y+dy[didx]
    if nx<0 or nx>=bx or ny<0 or ny>=by:
        break
    elif board[nx][ny]=='#':
        didx+=1
        didx%=4
    else:
        if board[nx][ny]=='.':
            if (nx,ny) not in ans and (x,y,didx) not in done:
                if fun(x,y,didx):
                    ans.add((nx,ny))
                done.add((x,y,didx))
            board[nx][ny]='X'
        x,y=nx,ny
print(len(ans))
f.close()