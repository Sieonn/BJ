def solution(my_string):
    result = ""
    return sorted([my_string[i:] for i in range(len(my_string))])
print(solution("banana"))