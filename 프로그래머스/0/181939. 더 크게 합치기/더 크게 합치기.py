def solution(a, b):
    num1 = str(a)+str(b)
    num2 = str(b)+str(a)
    return int(max(num1, num2))
# def solution(a, b):
#     return int(max(f"{a}{b}", f"{b}{a}"))