import sys
from collections import deque
input = sys.stdin.readline

def positionChange():
    dx = [-2, -2, -1, -1, 1, 1, 2, 2]
    dy = [-1, 1, -2, 2, -2, 2, -1, 1]
    q  = deque()
    q.append((sx,sy))
    while q:
        x, y = q.popleft()
        if x == mx and y == my:
            return board[x][y] -1
        for i in range(8):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx< bLen and 0 <= ny and board[nx][ny] ==0:
                board[nx][ny] = board[nx][ny] + 1
                q.append((nx, ny))


tc = int(input().strip())
for i in range(tc):
    bLen = int(input().strip())
    sx, sy = map(int, input().strip().split())
    mx, my = map(int, input().strip().split())
    board = [[0]*bLen for _ in range(bLen)]
    board[sx][sy] = 1
    print(positionChange())