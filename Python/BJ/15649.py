# 자연수 N과 M이 주어졌을 때, 아래 조건을 만족하는 길이가 M인 수열을 모두 구하는 프로그램을 작성
# 1부터 N까지 자연수 중에서 중복 없이 M개를 고른 수열

def dfs():
    if len(a)==M:
        print(' '.join(map(str,a)))
        return
    for i in range(1,N+1):
        if visited[i]:
            continue
        visited[i] = True
        a.append(i)
        dfs()
        a.pop()
        # print(a)
        # print(visited)
        visited[i] =False 
N, M = map(int, input().split())
a = []
visited = [False]*(N+1)
dfs()