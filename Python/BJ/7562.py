from collections import deque
import sys
input = sys.stdin.readline

#테스트 케이스를 받음
tc = int(input().strip())

def positionChange(): 
    #움직이는 방향을 나타냄
    dx = [-1, 1, 2, 2, 1, -1, -2, -2] 
    dy = [2, 2, 1, -1, -2, -2, -1, 1]
    
    
    q  = deque()
    q.append((sx,sy)) #시작점을 넣어준다.
    while q: #q가 비어있지 않다면 실행한다.
        x, y = q.popleft() #x, y는 현재 나이트의 위치이다.
        if x == mx and y == my: #만약 현재 위치가 목표한 위치에 도달했다면  
            return board[x][y] #도달한 위치의 값에서 -1을 빼고 출력한다.
        for i in range(8): #이동할 수 있는 방향이 8방향이라서 8번 반복한다.
            nx = x + dx[i] 
            ny = y + dy[i]
            if 0 <= nx< bLen and 0 <= ny<bLen and board[nx][ny] ==0: 
                #nx, ny의 값이 체스판을 넘어가지 않고 현재 위치에 0이 들어있다면
                board[nx][ny] = board[x][y] + 1 #현재 위치에 갈 수 있는 방향이
                q.append((nx, ny))


for i in range(tc): #테스트 케이스 만큼 반복한다.
    bLen = int(input().strip()) #체스판의 길이가 주어진다.
    sx, sy = map(int, input().strip().split()) #현재 나이트가 있는 위치가 주어진다.
    mx, my = map(int, input().strip().split()) #나이트가 최종적으로 도착해야할 위치가 주어진다.
    board = [[0]*bLen for _ in range(bLen)] # bLen X bLen 크기의 체스판을 생성한다.
    # board[sx][sy] = 1 #현재 나이트가 있는 위치에 1을 넣는다.
    print(positionChange()) # 함수를 실행한다.

2644
11724
2583
10026