
#N과 M이 주어졌을때, 아래 조건을 만족하는 길이가 M인 
# 수열을 모두 구하는 프로그램 작성
# 1부터 N까지 중에 M개 뽑기

# def NM(a, arr, index,cnt):
#     if cnt == M:
#         print(*a)
#         return 

#     for i in range(index, M):
#         a[cnt] = arr[i]
#         NM(a, arr,i+1, cnt+1)
# arr = []        
# while True:
#     # s = list(map(int, input().split()))
    
#     N, M = map(int, input().split())
# #1부터 N까지 배열 생성
#     for i in range(1, N+1):
#         arr.append(i)
# # NM(a, arr, 0, 0 )
#     if arr[0]==0:
#         break
#     a = [0]*(M+1)
#     NM(a, arr, 0, 0)
#     print()        
        
        
        
# # a = [0]*M

# arr = [] #1부터 N까지 배열 생성
# for i in range(1, N+1):
#     arr.append(i)
# NM(a, arr, 0, 0 )

# 자연수 N과 M이 주어졌을 때, 아래 조건을 만족하는 길이가 M인 수열을 모두 구하는 프로그램을 작성하시오.

# 1부터 N까지 자연수 중에서 중복 없이 M개를 고른 수열
# 고른 수열은 오름차순이어야 한다.

def dfs(arr,N, M, i):
    if len(arr)==M:
        print(*arr)
        return
    for i in range(i, N+1):
        arr.append(i)
        dfs(arr,N, M, i+1)
        arr.pop()

arr=[]
N, M = map(int, input().split())
dfs(arr,N,M,1)

# 미친.. 내가 이걸 풀다니..ㅠㅠㅠ