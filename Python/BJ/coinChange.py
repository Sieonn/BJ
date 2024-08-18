def coinChange(coins, amount):
    dp =  [float('inf') * (amount+1)]
    # float('inf') 양의 무한대 /  float('-inf')음의 무한대
    # 최대, 최소값을 구할 때 자주 사용
    
    #0원을 만들기 위해 필요한 동전의 수는 0(초기조건)
    dp[0] = 0
    
    for coin in coins:#[1, 2, 5]
        for i in range(coin, amount+1): #((1/ 2/ 5), 11+1)
            # 현재 금액 x에서 동전 coin을 뺀 금액의 dp 값에 +1(현재 동전 사용)
            dp[i] = min(dp[i], dp[i-coin]+1) 
    # 원하는 금액을 만들 수 없는 경우 -1반환 , 그렇지 않으면 총액 반환
    return dp[amount] if dp[amount] != float('inf') else -1

coins = [1, 2, 5]
amount = int(input())
print(coinChange(coins, amount))


# range(1, 11+1) => 1원으로 만들 수 있는 방법
# dp[1] = 1
# dp[2] = 2
# dp[3] = 3
# dp[4] = 4
# dp[5] = 5
# dp[6] = 6
# dp[7] = 7
# dp[8] = 8
# dp[9] = 9
# dp[10] = 10
# dp[11] = 11

#range(2, 11+1), coin = 2
# dp[2] = min(dp[2],dp[i-coin]+1) =min(dp[2], dp[0]+1) , min(2, 1)
# dp[2] = 1 => 2원이 있으니까 1원 두개 보다 2원 하나 쓰는게 더 최소의 방법
# dp[3] = 2
# dp[4] = 2
# ... 이런식으로 가면서 횟수가 줄어든다.


