def solution(n):
    result = []
    for i in range(n):
        answer = []
        for j in range(n):
            if i == j:
                answer.append(1)
            else:
                answer.append(0)
        result.append(answer)
    return result