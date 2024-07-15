import sys
input = sys.stdin.readline
N,M = map(int,input().split())
memo=[]
for _ in range(N):
    strr = list(input().split())
    memo.append(strr)

def findpw(memo, web):
    for i in memo:
        # print(i, web,"찾으려는 값" , i[0])
        if i[0]==web:
            # print(i[1])
            return i[1]
for _ in range(M):
    pw = findpw(memo,  input())
    print(pw)