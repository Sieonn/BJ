import sys
from collections import deque

N = int(sys.stdin.readline())
que = deque()
for i in range(N):
    s = sys.stdin.readline().split()
    if s[0] == "push":
        que.insert(0,int(s[1]))
    if s[0] =="pop":
        if len(que) !=0:
            print(que[-1])
            que.pop()
        else:
            print(-1)
    if s[0] == "front":
        if len(que) !=0:
            print(que[-1])
        else:
            print(-1)
    if s[0] =="size":
        print(len(que))
    if s[0] =="empty":
        if len(que)==0:
            print(1)
        else:
            print(0)
    if s[0] =="back":
        if len(que) != 0:
            print(que[0])
        else: 
            print(-1)