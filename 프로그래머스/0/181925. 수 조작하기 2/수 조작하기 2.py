def solution(numLog):
    num = numLog[0]
    result = ""
    for i in numLog[1:]:
        num = i - num
        if num == 1:
            result += "w"
        elif num == -1:
            result += "s"
        elif num == 10:
            result += "d"
        else:
            result += "a"
        num = i
    return result