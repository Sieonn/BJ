# def solution(array):
#     if len()
    
# print(solution([1, 2, 3, 3, 3, 4]))

# import math
# n=144

# b= int(math.sqrt(n))
# n%b==0
# if type(b) == int:
    
#     print(b)
# else:
#     print("no")

# listd = ["1", "2", "g"]
# liste = ["1", "3", "4", "g"]
# list2 = set(liste+listd)
# print(list2)

# def solution(numbers, direction):
#     return numbers[-1] + numbers[:-1] if direction == "right" else numbers[1:] + numbers[0]
# print(solution([1, 2, 3], "right"))

# def solution(numbers, direction):
#     return numbers[-1] + numbers[:len(numbers)-1] if direction == "right" else numbers[1:] + numbers[0]
# print(solution([1, 2, 3], "right"))

# listd = [1, 2, 3]
# print(listd[1])
# def solution(age):
#     new = ""
#     for i in str(age):
#         print(ord(i), i)
#         new += chr(ord(i)+47)
#     return new
# print(solution(23))

def solution(emergency):
    arr = {}
    
    for j,k in enumerate(sorted(emergency)):
        arr[k] = len(emergency)-j
        print(arr)
    arr2 =[]
    for i in emergency:
        arr2 += [arr[i]]
    return arr2
print(solution([3, 72,24]))