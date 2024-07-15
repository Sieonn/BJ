import sys
input = sys.stdin.readline
N,M = map(int,input().split())
memo=[]
for _ in range(N):
    strr = list(input().split())
    memo.append(strr)

def findpw(memo, web):
    for i in memo:
        if i[0] == web:
            return i[1]
        
for _ in range(M):
    pw = findpw(memo,  input())
    print(pw)