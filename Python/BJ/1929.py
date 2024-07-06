# N, M= map(int, input().split())
# cnt=0
# for i in range(N, M+1):
#     for j in range(1, i+1):
#         if(i%j==0):
#             cnt+=1
            
#     if(cnt>2):
#         cnt=0
#     else:
#         print(i)      =>시간 초과 뜬다.
# -------------------------------------------
# N, M = map(int, input().split())

# for i in range(N, M+1):
#     if i == 1: # 1은 통과
#         continue
        
#     for j in range(2, int(i**0.5) + 1): # 2 ~ 제곱근 사이 값 확인
#         if i % j == 0: # 나누어 떨어진다면 그대로 종료 (else문 실행 X)
#             break
#     else: # for문이 잘 실행이 되었다면 print(i) 출력
#         print(i)


#-------------------------------
N = int(input())
arr = list(map(int, input().split()))
cnt=0
for i in arr:
    if i==1:
        continue
    for j in range(2, int(i**0.5)+1):
        if i% j==0:
            break
    else:
        cnt+=1
print(cnt)
# for i in N:
    