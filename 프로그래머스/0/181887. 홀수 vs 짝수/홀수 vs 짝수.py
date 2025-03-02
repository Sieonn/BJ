# def solution(num_list):
#     even = 0
#     odd = 0
#     for i,v  in enumerate(num_list):
#         if i % 2 == 0:
#             odd += v
#         else:
#             even += v
#     return max(odd, even)

def solution(num_list):
    return max(sum(num_list[::2]), sum(num_list[1::2]))