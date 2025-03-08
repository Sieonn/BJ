def solution(num_list):
    a = 1
    for i in num_list:
        a *= i
    return int(sum(num_list)**2 > a)
print(solution([3,4,5,2,1]))