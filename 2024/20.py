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
sys.setrecursionlimit(3*(10**5))
f=open("1210.in","r")

MI = lambda: map(int, f.readline().split())
LI = lambda: list(map(int, f.readline().split()))
II = lambda: int(f.readline())
IR = lambda: f.readline().rstrip()
LIR = lambda: list(f.readline().rstrip())
LIRS = lambda: list(f.readline().rstrip().split())
INF = math.inf

board=[]
while True:
    temp=list(map(int,LIR()))
    if not temp:
        break
    board.append(temp)
h,w=len(board), len(board[0])

dx=[0,1,0,-1]
dy=[1,0,-1,0]

def hike(row, col, height, visited):
    global ans
    for k in range(4):
        nx,ny=row+dx[k],col+dy[k]
        if nx<0 or ny<0 or nx>=h or ny>=w or visited[nx][ny] or board[nx][ny]!=height+1:
            continue
        #visited[nx][ny]=True
        if height+1 == 9:
            ans+=1
        hike(nx,ny,height+1,visited)

def slope(row, col):
    visited=[[False]*w for _ in range(h)]
    visited[row][col]=True
    hike(row,col,0,visited)

ans=0
for i in range(h):
    for j in range(w):
        if board[i][j]==0:
            slope(i,j)
print(ans)
f.close()