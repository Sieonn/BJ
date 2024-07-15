import sys
import math
# N=동생수, S =수빈이 위치
N, S = map(int, input().split())
A1 = list(map(int, input().split()))

# 엘리베이터 문제인 스타트링크 문제와 유사
# 모든 도생을 찾기 위한 공통적인 약수의 최대값을 구해야함
# => 동생과의 거리의 최대 공약수 구하기
A2 = list(map(lambda x: abs(x-N),A1))
# for i, v in enumerate(A1):
#     A1[i] = abs(v-N)
def sum(A,B):
    while B!= 0:
        A, B= B, A%B
    print(A)
    return A
for i in range(len(A2)):
    sum(A2[0], A2[1])
    del A2[1]                  
    # print(A2)    

