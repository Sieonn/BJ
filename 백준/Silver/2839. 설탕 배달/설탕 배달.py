def suga(bags, amount):
    dp = [float('inf')]*(amount+1)
    
    dp[0] = 0
    
    for i in bags:
        for j in range(i, amount+1):
            dp[j] = min(dp[j], dp[j-i]+1)
    return dp[amount] if dp[amount] != float('inf')  else -1    

bags = [3,5]
amount = int(input()) 
print(suga(bags, amount))   