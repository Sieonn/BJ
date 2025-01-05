# def binary(bin):
#     num = 0
#     for i, v in enumerate(bin):
#         if v == "1":
#             num += 2 ** (len(bin) - i -1)
#     return num
# def solution(bin1, bin2):
#     if bin1 == "0" and bin2 == "0":
#         return "0"
#     answer = ""
#     bin3 = binary(bin1) + binary(bin2)
#     while bin3 >= 2 :
#         if bin3 % 2 == 0:
#             bin3 = bin3 // 2
#             answer += "0"
#         else:
#             bin3= bin3 // 2
#             answer += "1"
#     answer += "1"
#     return answer[::-1]
def solution(bin1, bin2):
    answer = bin(int(bin1,2) + int(bin2,2))[2:]
    return answer

print(solution("10", "11"))