import math
from decimal import *

f = open("1204.in", "r")
MI = lambda: map(int, f.readline().split())
LI = lambda: list(map(int, f.readline().split()))
II = lambda: int(f.readline())
IR = lambda: f.readline().rstrip()
LIR = lambda: list(f.readline().rstrip())
LIRS = lambda: list(f.readline().rstrip().split(""))
INF = math.inf
# sys.setrecursionlimit(3*(10**5))
# getcontext().prec=100


ans = 0
board = []
while True:
    try:
        IN = LIR()
        if not IN:
            raise EOFError
        board.append(IN)
    except:
        break
dx = [-1, -1, -1, 0, 0, 1, 1, 1]
dy = [-1, 0, 1, -1, 1, -1, 0, 1]
for i in range(len(board)):
    for j in range(len(board[0])):
        if board[i][j] != "@":
            continue
        cnt = 0
        for k in range(8):
            nx, ny = i + dx[k], j + dy[k]
            if 0 <= nx < len(board) and 0 <= ny < len(board[0]):
                if board[nx][ny] == "@":
                    cnt += 1
                    if cnt >= 4:
                        break
        if cnt < 4:
            ans += 1
print(ans)
