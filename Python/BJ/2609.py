# //두 개의 자연수를 입력받아 최대 공약수와 최소 공배수를 출력
# lista= list(map(int, input().split()))
# max=[]
# max2=[]
# for i,v in enumerate(lista):
#     for j in range(1,v+1):
#         if(v%j==0 and v == lista[0]):
#             max.append(j)
#         elif(v%j==0 and i==1):
#             max2.append(j)      
# a= list(set(max) & set(max2)) #두 리스트 사이에 겹치는 수만
# b=a[-1] #최대 공약수
# c = (lista[0]//b)*(lista[1]//b)*b
# print(b, c, sep="\n")


def gcd(a, b):
    while b !=0:
        a, b = b, a %b
    return a
def lcm(a, b):
    return a*b//gcd(a,b)

a, b =  map(int, input().split())
g = gcd(a, b)
l = lcm(a, b)
print(g, l, sep="\n")

# def gcd(a, b):
#     while b != 0:
#         a, b = b, a % b
#     return a

# def lcm(a, b):
#     return a * b // gcd(a, b)

# # 입력 받기
# a, b = map(int, input().split())

# # 최대공약수와 최소공배수 구하기
# g = gcd(a, b)
# l = lcm(a, b)

# # 결과 출력
# print(g)
# print(l)
