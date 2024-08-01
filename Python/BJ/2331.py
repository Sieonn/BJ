
import sys
from collections import deque

input =  sys.stdin.readline
A, P = map(str,input().strip().split())
result = deque()
result.append(A)

start = A
while len(result)>0:
    val=0
    for i in start:
        val += int(i)**int(P)
    print(result)      
    if str(val) in result:
        B = result.index(str(val))
        print(B)
        break
    else:
        result.append(str(val))
        start = str(val)
