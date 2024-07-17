import sys
input = sys.stdin.readline

def arr_sum(arr, target):
    left, cur_sum, cnt = 0, 0, 0
    for right in range(N):
        cur_sum += arr[right]
        
        while cur_sum > target and left <= right:
            cur_sum -= arr[left] 
            #만약 0부터i까지 더했다면, 가장 작은 수를 빼줘서 target과 일치하는지 확인
            left +=1
        if cur_sum ==target:
            cnt+=1
            
    return cnt

N, M = map(int, input().strip().split())
arr = list(map(int, input().strip().split()))

print(arr_sum(arr, M))