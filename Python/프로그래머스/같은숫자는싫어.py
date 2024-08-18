def solution(arr):
    arr2=[arr[0]]
    for i in range(1, len(arr)):
        if arr[i] != arr[i-1]:
            arr2.append(arr[i])
    print(arr2)
solution([4,4,4,3,3])