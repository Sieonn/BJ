
#N과 M이 주어졌을때, 아래 조건을 만족하는 길이가 M인 
# 수열을 모두 구하는 프로그램 작성
# 1부터 N까지 중에 M개 뽑기

def NM(a, arr, index,cnt):
    if cnt == M:
        print(*a)
        return 

    for i in range(index, M):
        a[cnt] = arr[i]
        NM(a, arr,i+1, cnt+1)
        
while True:
    # s = list(map(int, input().split()))
    
    N, M = map(int, input().split())
    arr = [] #1부터 N까지 배열 생성
    for i in range(1, N+1):
        arr.append(i)
# NM(a, arr, 0, 0 )
    if arr[0]==0:
        break
    a = [0]*M
    NM(a, arr, 0, 0)
    print()        
        
        
        
# a = [0]*M

arr = [] #1부터 N까지 배열 생성
for i in range(1, N+1):
    arr.append(i)
NM(a, arr, 0, 0 )