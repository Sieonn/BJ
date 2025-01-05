def solution(before, after):
    a = set(before)
    for i in a:
        if before.count(i) != after.count(i):
            return 0
    return 1
print(solution("allpe", "apple"))