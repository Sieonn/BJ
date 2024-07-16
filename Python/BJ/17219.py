import sys
input = sys.stdin.readline
N,M = map(int,input().strip().split())
memo= {}
for _ in range(N):
    web, password = input().strip().split()
    memo[web] = password

for _ in range(M):
    web = input().strip()
    print(memo[web])