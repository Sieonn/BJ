def solution(quiz):
    answer=[]
    for i in quiz:
        a = i.split("=")
        if eval(a[0]) == int(a[1]):
            answer.append("O")
        else:
            answer.append("X")
    return answer

print(solution(["19 - 6 = 13", "5 + 66 = 71", "5 - 15 = 63", "3 - 1 = 2"]))
    