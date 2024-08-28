# 머쓱이네 피자가게는 피자를 두 조각에서 열 조각까지 원하는 조각 수로 잘라줍니다. 피자 조각 수 slice와 피자를 먹는 사람의 수 n이 매개변수로 주어질 때, 
# n명의 사람이 최소 한 조각 이상 피자를 먹으려면 최소 몇 판의 피자를 시켜야 하는지를 return 하도록 solution 함수를 완성해보세요.

# def solution(slice, n):
#     #피자 조각보다 사람 수가 적을때
#     if slice >= n:
#         return 1
#     #피자 조각보다 사람 수가 많을때
#     else:
#         return slice//n if n%slice == 0 else slice//n + 1
# num=""
# for i in "a1bcd":
#     # num += i
#     if i.isdecimal(): 
#         print(i,type(i))

#     # print(i)
# # print("abd"[1])


# def solution(my_string):
#     sum = 0
#     num = ''
#     for i in my_string:
#         if i.isdecimal():
#             num+= str(i)
#             print(num)
#         else:
#             if num != '':
#                 sum += int(num)
#                 print(sum)
#                 num = ''
#     return sum

# print(solution("aAb1B2cC34oOp"))

# strA = "abdDDDS"
# new=""
# new2 = strA.swapcase()
# for i in strA:
#     new += i.swapcase()
# print(new, new2)

# lis = ["1", "2", "3" ]
# # A = max(lis)
# # B = lis.index(A)
# # print(A, B)

# A = ('').join(lis)
# print(A)

# def solution(numbers):
#     numbers.sort()
#     maxNum = 0
#     for i,v in enumerate(numbers[:-1]):
#         for j in range(i+1, len(numbers)):
#             maxNum = max(maxNum, v*numbers[j])
#     return maxNum
# print(solution([10, 20, 30, 5, 5, 20, 5]))
    
    
    # 403: 권한없음
    # 404: 해당 메소드 없음 or 네트워크 에러
    
def solution(my_string):
    new = []
    for i in my_string:
        if i.isdecimal():
            new.append(i)
    return new.sort

print(solution("ab12345"))