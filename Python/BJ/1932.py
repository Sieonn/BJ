# # 정수 삼각형
# #현재 수에서 왼쪽 혹은 오른쪽만 선택가능 => 가운데 선택

# import sys
# import math
# input = sys.stdin.readline;
# def triangle(D):
#     dp = [[0] * D for i in range(D)]
#     #일단 D단계 내려가니까 생성
#     dp[0][0] = paths[0][0]
#     for i in range(1,D):
#         for j in range(len(paths[i])):
#             #i=2 j=1
#             dp[i][j] = max(dp[i-1][j-1]+paths[i][j], dp[i-1][j]+paths[i][j])
#     return max(dp[D-1])
# D = int(input().strip());
# paths = []
# for i in range(D):
#     paths.append(list(map(int, input().strip().split())));
# print(triangle(D))

vars = [[1, 1, 0], 
        [2, 3, 0], 
        [3, 4, 5]]
print(vars[1][-1])