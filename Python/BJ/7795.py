# import sys
# input = sys.stdin.readline
# tc  = int(input().strip())
# for _ in range(tc):
#     A,B = map(int, input().strip().split())
#     Aarr = sorted(list(map(int, input().strip().split())),reverse=True)
#     Barr = sorted(list(map(int, input().strip().split())))
#     cunt = 0
#     for i in Aarr:
#         for j in Barr:
#             if i> j:
#                 cunt+=1
#             elif i<=j:
#                 break
#     print(cunt)

# 시간초과 발생
# 이진탐색을 사용해서 풀이
import sys
import bisect


