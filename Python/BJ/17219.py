import sys
input = sys.stdin.readline
N,M = map(int,input().strip().split())
memo= {}
for _ in range(N):
    web, password = input().strip().split()
    memo[web] = password

def findpw(memo, web):
    for i in memo:
        if i[0] == web:
            return i[1]
        
for _ in range(M):
    pw = findpw(memo,  input().strip())
    print(pw)