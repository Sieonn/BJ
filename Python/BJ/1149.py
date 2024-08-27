def rgb_distance(costs):
    n = len(costs)
    dp = [[0] * 3 for _ in range(n)]
    
    # 첫 번째 집의 초기 비용 설정
    dp[0][0] = costs[0][0]  # 빨강
    dp[0][1] = costs[0][1]  # 초록
    dp[0][2] = costs[0][2]  # 파랑
    
    # 두 번째 집부터 마지막 집까지 최소 비용 계산
    for i in range(1, n):
        dp[i][0] = min(dp[i-1][1], dp[i-1][2]) + costs[i][0]  # 빨강
        dp[i][1] = min(dp[i-1][0], dp[i-1][2]) + costs[i][1]  # 초록
        dp[i][2] = min(dp[i-1][0], dp[i-1][1]) + costs[i][2]  # 파랑
    
    # 마지막 집에서 최소 비용 선택
    return min(dp[-1][0], dp[-1][1], dp[-1][2])

# 입력 처리
n = int(input())
costs = [list(map(int, input().split())) for _ in range(n)]

# 결과 출력
print(rgb_distance(costs))
