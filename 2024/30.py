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
    newIN=[]
    for c in IN:
        if c=='#':
            newIN.append('#')
            newIN.append('#')
        elif c=='O':
            newIN.append('[')
            newIN.append(']')
        elif c=='.':
            newIN.append('.')
            newIN.append('.')
        else:
            newIN.append('@')
            newIN.append('.')
    board.append(newIN)
    if y==-1:
        x+=1
        if '@' in IN:
            y=newIN.index('@')
print(x,y)

def fun(x,y,ax,ay,c):
    if board[x+ax][y+ay]=='[':
        ret=fun(x+ax,y+ay,ax,ay,'[')
        if ret:
            board[x+ax][y+ay]=c
        return ret
    elif board[x+ax][y+ay]==']':
        ret=fun(x+ax,y+ay,ax,ay,']')
        if ret:
            board[x+ax][y+ay]=c
        return ret
    elif board[x+ax][y+ay]=='.':
        board[x+ax][y+ay]=c
        return True
    else:
        return False
    
def fun_updown_chk(x,y,ax,ay):
    if board[x+ax][y+ay]=='[':
        ret=fun_updown_chk(x+ax,y+ay,ax,ay)
        ret2=fun_updown_chk(x+ax,y+ay+1,ax,ay)
        return ret&ret2
    elif board[x+ax][y+ay]==']':
        ret=fun_updown_chk(x+ax,y+ay,ax,ay)
        ret2=fun_updown_chk(x+ax,y+ay-1,ax,ay)
        return ret&ret2
    elif board[x+ax][y+ay]=='.':
        return True
    else:
        return False
    
def fun_updown(x,y,ax,ay,c):
    if board[x+ax][y+ay]=='[':
        board[x+ax][y+ay]=c
        board[x+ax][y+ay+1]='.'
        ret=fun_updown(x+ax,y+ay,ax,ay,'[')
        ret2=fun_updown(x+ax,y+ay+1,ax,ay,']')
        return ret&ret2
    elif board[x+ax][y+ay]==']':
        board[x+ax][y+ay]=c
        board[x+ax][y+ay-1]='.'
        ret=fun_updown(x+ax,y+ay,ax,ay,']')
        ret2=fun_updown(x+ax,y+ay-1,ax,ay,'[')
        return ret&ret2
    elif board[x+ax][y+ay]=='.':
        board[x+ax][y+ay]=c
        return True
    else:
        return False

while True:
    IN=IR()
    if not IN:
        break
    for c in IN:
        if c=='^':
            if fun_updown_chk(x,y,-1,0):
                fun_updown(x,y,-1,0,'@')
                board[x][y]='.'
                x-=1
        elif c=='>':
            if fun(x,y,0,1,'@'):
                board[x][y+1]='@'
                board[x][y]='.'
                y+=1
        elif c=='v':
            if fun_updown_chk(x,y,1,0):
                fun_updown(x,y,1,0,'@')
                board[x][y]='.'
                x+=1
        elif c=='<':
            if fun(x,y,0,-1,'@'):
                board[x][y-1]='@'
                board[x][y]='.'
                y-=1
        # for i in board:
        #     print(*i,sep='')

ans=0
for i in range(len(board)):
    for j in range(len(board[0])):
        if board[i][j]=='[':
            ans+=100*i+j
print(ans)


f.close()