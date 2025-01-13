def solution(spell, dic):
    for i in dic:
        answer = []
        for k in spell:
            if i.count(k) == 1:
                answer.append(1)
        if len(answer) == len(spell):
            return 1
    return 2  