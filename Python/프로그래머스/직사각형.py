def solution(dots):
    x=dots[0][0]
    y=dots[0][1]
    for i in dots[1:]:
        if i[0] != x:
            x1 = x - i[0]
        if i[1] != y:
            y1 = y - i[1]
    return abs(x1) * abs(y1)

print(solution([[-1, -1], [1, 1], [1, -1], [-1, 1]]))           