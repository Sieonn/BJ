def minPathSum(grid):
    m,n = len(grid), len(grid[0]) #행 열  3,3
    
    dp = [[0]* n  for _ in range(m)]
    #그리드의 각 열의 이동 방법 저장
    #=>
    # [[0, 0, 0],
    #  [0, 0, 0],
    #  [0, 0, 0]]
    dp[0][0] = grid[0][0]
    # [[1, 0, 0],
    #  [0, 0, 0],
    #  [0, 0, 0]]
    # 첫 번째 열의 최소 비용
    for i in range(1, m): 
        dp[i][0] = dp[i-1][0]+ grid[i][0] # 1, 1, 4
    # [[1, 0, 0],
    #  [2, 0, 0],
    #  [6, 0, 0]]
    
    for j in  range(1, n):
        dp[0][j] =  dp[0][j-1] + grid[0][j] #1, 3, 1
    # [[1, 4, 5],
    #  [2, 0, 0],
    #  [6, 0, 0]]
    
    for i in range(1, m):
        for j in range(1, n):
            dp[i][j] = min(dp[i-1][j], dp[i][j-1])+ grid[i][j]        
    # [[1, 4, 5],
    #  [2, 2+5, 6],
    #  [6, 8, 7]]
    return dp[m-1][n-1]
grid = [
    [1, 3, 1],
    [1, 5, 1],
    [4, 2, 1]
]
print(minPathSum(grid))