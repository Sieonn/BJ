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