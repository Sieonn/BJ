def solution(array, n):
    array = sorted(array)
    newArr = list(map(lambda x : abs(x - n), array))
    num = newArr.index(min(newArr))
    return array[num]
print(solution([3, 10, 28, 12], 20))
