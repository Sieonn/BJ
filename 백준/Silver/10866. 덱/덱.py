from collections import deque
import sys
input = sys.stdin.readline


n = int(input().strip())
d = deque()
for _ in range(n):
    state = list(input().strip().split())
    if state[0] =="push_back":
        d.append(int(state[1]))
    elif state[0] =="push_front":
        d.appendleft(int(state[1]))
    elif state[0] == "pop_front":
        if len(d)==0:
            print(-1)
        else:
            print(d[0])
            d.popleft()
    elif state[0] =="pop_back":
        if len(d)==0:
            print(-1)
        else:
            print(d[-1])
            d.pop()
    elif state[0] =="size":
        print(len(d))
    elif state[0] =="empty":
        if len(d):
            print(0)
        else: print(1)
    elif state[0]=="front":
        if len(d)==0:
            print(-1)
        else:
            print(d[0])
    elif state[0]=="back":
        if len(d)==0:
            print(-1)
        else:
            print(d[-1])