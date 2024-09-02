def solution(num):
    pos = []
    neg = []
    result = 0
    for i in num:
        if n <= 0:
            neg.append(i)
        elif n > 1:
            pos.append(i)
        else:
            result += 1
    neg.sort()
    pos.sort(reverse=True)
    
        # 양수 처리 (2개씩 묶어 곱셈)
    result += sum(pos[i] * pos[i + 1] for i in range(0, len(pos) - 1, 2))
    if len(pos) % 2 == 1:
        result += pos[-1]

    # 음수 처리 (2개씩 묶어 곱셈)
    result += sum(neg[i] * neg[i + 1] for i in range(0, len(neg) - 1, 2))
    if len(neg) % 2 == 1:
        result += neg[-1]
    return result


n = int(input())
num = [int(input()) for _ in  range(n)]    
    