import sys
from collections import deque
input = sys.stdin.readline


def dfs(graph, start, visited): #dfs 함수
    queue =deque([start])
    visited[start] = 1
    
    while queue:
        v = queue.popleft()
        for i in graph[v]:
            if visited[i] == 0:
                queue.append(i)
                visited[i] == 1
        
N, M  = map(int, input().strip().split())
graph = [[] for _ in range(N+1)]
visited = [0] * (N+1)

for _ in range(M):
    U, V = map(int, input().strip().split())
    graph[U].append(V)
    graph[V].append(U)
    
count = 0 #그래프 수
for i in range(1, N+1):
    if visited[i] == 0:
        dfs(graph, i, visited) #여기서 생성한 그래프를 돌면서 확인한다.
        count += 1
        
print(count)







# 다른 풀이
from collections import deque
import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

# bfs 함수
def bfs(graph, start, visited):
    queue = deque([start])
    visited[start] = True

    while queue:
        v = queue.popleft()
        for i in graph[v]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True

n, m = map(int, input().split()) # 정점의 개수, 간선의 개수
graph = [[] for _ in range(n+1)]
for i in range(m):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

count = 0 # 연결 노드의 수
visited = [False] * (n+1)
for i in range(1, n+1):
    if not visited[i]:
        bfs(graph, i, visited) # bfs 한 번 끝날 때마다 count+1
        count += 1

print(count)