def solution(hp):
    ants = [5, 3, 1]
    i = 0
    count = 0
    if hp == 0:
        return 0
    while(hp != 0):
        if hp >= ants[i]:
            count += hp//ants[i]
            hp = hp%ants[i]
        else:
            i += 1
    return count