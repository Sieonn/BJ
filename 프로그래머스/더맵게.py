# import heapq

# def solution(scoville, k):
#     heap = []
#     for i in scoville:
#         heapq.heappush(heap, i)
        
#     cnt = 0 
#     while heap[0] < k:
#         try:
#             heapq.heappush(heap, heapq.heappop(heap)+ heapq.heappop(heap)*2)
#         except IndexError:
#             return -1
#         cnt+=1
#     return cnt

# print(solution([1, 2, 3, 9, 10, 12],7))

import heapq as hq
 
def solution(scoville, k):
    
    hq.heapify(scoville)
    answer = 0
    while True:
        first = hq.heappop(scoville)
        if first >= k:
            break
        if len(scoville) ==0:
            return -1
        second =hq.heappop(scoville)
        hq.heappush(scoville, first+second*2)
        answer += 1
    return answer    

print(solution([1, 2, 3, 9, 10, 12], 7))