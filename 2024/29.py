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
f=open("1215.in","r")

MI = lambda: map(int, f.readline().split())
LI = lambda: list(map(int, f.readline().split()))
II = lambda: int(f.readline())
IR = lambda: f.readline().rstrip()
LIR = lambda: list(f.readline().rstrip())
LIRS = lambda: list(f.readline().rstrip().split())
INF = math.inf

board=[]
x,y=-1,-1
while True:
    IN=LIR()
    if not IN:
        break
    board.append(IN)
    if y==-1:
        x+=1
        if '@' in IN:
            y=IN.index('@')
print(x,y)

def fun(x,y,ax,ay):
    if board[x+ax][y+ay]=='O':
        return fun(x+ax,y+ay,ax,ay)
    elif board[x+ax][y+ay]=='.':
        board[x+ax][y+ay]='O'
        return True
    else:
        return False

while True:
    IN=IR()
    if not IN:
        break
    for c in IN:
        if c=='^':
            if fun(x,y,-1,0):
                board[x-1][y]='@'
                board[x][y]='.'
                x-=1
        elif c=='>':
            if fun(x,y,0,1):
                board[x][y+1]='@'
                board[x][y]='.'
                y+=1
        elif c=='v':
            if fun(x,y,1,0):
                board[x+1][y]='@'
                board[x][y]='.'
                x+=1
        elif c=='<':
            if fun(x,y,0,-1):
                board[x][y-1]='@'
                board[x][y]='.'
                y-=1

ans=0
for i in range(len(board)):
    for j in range(len(board[0])):
        if board[i][j]=='O':
            ans+=100*i+j
print(ans)


f.close()