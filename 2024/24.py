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
f=open("1212.in","r")

MI = lambda: map(int, f.readline().split())
LI = lambda: list(map(int, f.readline().split()))
II = lambda: int(f.readline())
IR = lambda: f.readline().rstrip()
LIR = lambda: list(f.readline().rstrip())
LIRS = lambda: list(f.readline().rstrip().split())
INF = math.inf

def find(x):
    if parent[x]==x:
        return x
    parent[x]=find(parent[x])
    return parent[x]

def union(x,y):
    x=find(x)
    y=find(y)
    if x==y:
        return False
    parent[x]=y
    return True

board=[]
while True:
    a=LIR()
    if not a:
        break
    board.append(a)
h,w=len(board),len(board[0])

dx=[0,1,0,-1]
dy=[1,0,-1,0]

def fun(x, y, c):
    global cnt
    for border in [(x,y,1),(x+1,y,1),(x,y,0),(x,y+1,0)]:
        if border in ns:
            continue
        elif border in s:
            s.remove(border)
            ns.add(border)
        else:
            s.add(border)
    cnt+=1
    for i in range(4):
        nx=x+dx[i]
        ny=y+dy[i]
        if nx<0 or ny<0 or nx>=h or ny>=w or visited[nx][ny] or board[nx][ny]!=c:
            continue
        visited[nx][ny]=True
        fun(nx,ny,c)

ans=0
visited=[[False]*w for _ in range(h)]
for i in range(h):
    for j in range(w):
        if visited[i][j]:
            continue
        s=set([])
        ns=set([])
        cnt=0
        visited[i][j]=True
        fun(i,j, board[i][j])
        ls=list(s)
        parent=[ii for ii in range(len(ls))]
        ds=defaultdict(int)
        idx=0
        for ii in ls:
            ds[ii]=idx
            idx+=1
        sides=len(s)
        for idx,(q,ww,e) in enumerate(ls):
            if e==0:    # |
                if (q-1,ww,e) in s:
                    #print(q,ww,e, h, w)
                    if 0<q<h and ((ww<w and board[q-1][ww]==board[q][ww]==board[i][j]) or (ww>0 and board[q-1][ww-1]==board[q][ww-1]==board[i][j])):
                        if union(ds[(q-1,ww,e)],idx):
                            sides-=1
                if (q+1,ww,e) in s:
                    if 0<=q<h-1 and ((ww<w and board[q+1][ww]==board[q][ww]==board[i][j]) or (ww>0 and board[q+1][ww-1]==board[q][ww-1]==board[i][j])):
                        if union(ds[(q+1,ww,e)],idx):
                            sides-=1
            else:       # -
                if (q,ww-1,e) in s:
                    if 0<ww<w and ((q<h and board[q][ww-1]==board[q][ww]==board[i][j]) or (q>0 and board[q-1][ww-1]==board[q-1][ww]==board[i][j])):
                        if union(ds[(q,ww-1,e)],idx):
                            sides-=1
                if (q,ww+1,e) in s:
                    if 0<=ww<w-1 and ((q<h and board[q][ww+1]==board[q][ww]==board[i][j]) or (q>0 and board[q-1][ww+1]==board[q-1][ww]==board[i][j])):
                        if union(ds[(q,ww+1,e)],idx):
                            sides-=1
        ans+=cnt*sides
        #print(cnt,sides,board[i][j])
print(ans)

f.close()