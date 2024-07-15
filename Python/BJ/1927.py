# import sys;
# input = sys.stdin.readline
# N = int(input())
# arr = []
# def minremove(arr):
#     if len(arr) ==0:
#         return 0
#     min = arr[0]
#     for i in arr:
#          if i < min:
#              min = i
#     return min
# for i in range(N):
#     X = int(input())
#     if X>0:
#         arr.append(X)
#     else:
#         min = minremove(arr)
#         print(min)
#         if len(arr) !=0:
#             arr.remove(min)

import sys
import heapq

input = sys.stdin.readline
N = int(input())

heap = []

for i in range(N):
    X = int(input())
    if X > 0:
        heapq.heappush(heap, X)
    else:
        if heap:
            min = heapq.heappop(heap)
            print(min)
        else:
            print(0)