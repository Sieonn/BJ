from sys import stdin
input = stdin.readline
N = int(input())
Numlist = list(map(int, input().split()))
dp = [1]*N

for i in range(N):
	for j in range(i):
		if Numlist[i] > Numlist[j]:
			dp[i] = max(dp[i], dp[j]+1)
print(max(dp))