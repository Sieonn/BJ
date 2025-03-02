def solution(arr, n):
    if len(arr) % 2 == 1:
        for i in range(0,len(arr),2):
            arr[i] += n
    else:
        for i in range(1,len(arr),2) :
            arr[i] += n
    return arr
    
                
print(solution([444, 555, 666, 777], 100 ))