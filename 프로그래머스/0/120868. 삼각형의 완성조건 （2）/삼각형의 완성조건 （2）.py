def solution(sides):
    answer = []
    maxN = max(sides)
    minN = min(sides)
    # sides안에 담긴 수가 제일 긴 경우
    i = 1
    while 0 <i < maxN+minN:
        if maxN >= i >maxN - minN:
            if i not in answer:
                answer.append(i)
        elif maxN+minN > i >= maxN: 
            if i not in answer:
                answer.append(i)
        i+= 1
    return len(answer)