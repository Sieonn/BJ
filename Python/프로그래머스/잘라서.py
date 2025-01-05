# def solution(my_str, n):
#     l = len(my_str)
#     a = l//n
#     b = l%n
#     if b != 0:
#         a+=1
#     answer = []
#     for i in range(a):
#         if (i*n)+n > len(my_str):
#             answer.append(my_str[i*n:])
#         else:
#             answer.append(my_str[i*n:(i*n)+n])
#     return answer
def solution(my_str, n):
    return [my_str[i: i+n] for i in range(0, len(my_str),n)]
print(solution("abcdef123",3))