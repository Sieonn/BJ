# def solution(arr):
#     x = []
#     for i in arr:
#         for j in range(i):
#             x.append(i)
#     return x
            
def solution(arr):
    return [i for i in arr for j in range(i)]