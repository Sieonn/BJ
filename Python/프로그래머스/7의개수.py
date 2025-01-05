def solution(array):
    array = list(map(str, array))
    return ''.join(array).count("7")
print(solution([10, 29]))