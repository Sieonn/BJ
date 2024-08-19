import sys
input = sys.stdin.readline
tc = int(input())
def apt(k,n):
    dp = [[0]*(n+1) for _ in range(k+1)]
    for j in range(n+1):
        dp[0][j] = j
    for i in range(1,k+1): #1층
        for j in range(1,n+1): #1호 부터 4호 전까지
            for s in range(1,j+1):
                dp[i][j] += dp[i-1][s]
            #1-1 = 
    return dp[k][n]
for _ in range(tc):
    k = int(input())
    n = int(input())
    print(apt(k,n))
    
    
    #k층에 n호에 몇명사느냐
#최대 층고가 k라고 했을 때
#일단 0층의 i호에는 i명이 살고 호수는1부터 시작