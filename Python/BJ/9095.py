import sys
input = sys.stdin.readline
def plus(n):
    if n == 1:
        return 1
    elif n ==2:
        return 2
    elif n ==3 :
        return 4
    else:
        dp = [0]*(n+1)
        dp[1] = 1 
        dp[2] = 2 
        dp[3] = 4 #(1,1,1), (2+1), (1+2), (3)
        for i in range(4, n+1):
            dp[i] = dp[i-3]+ dp[i-2]+dp[i-1]
    return dp[n]
tc = int(input())
for i in range(tc):
    n=int(input())    
    print(plus(n))