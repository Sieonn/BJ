# import sys
# input = sys.stdin.readline

# C = int(input().strip())
# N = int(input().strip())
# A = []
# for i in range(0,int(N)):
#     K, V =  map(int, input().strip().split())
#     if K == 1:
#         A.append(V)
#     elif K in A:
#         A.append(V)
# print(len(set(A)))

# import sys
# from collections import deque

# input = sys.stdin.readline

# # 함수 밑에서 예시 입력으로 생성한 그래프 [[], [2, 5], [1, 3, 5], [2], [7], [1, 2, 6], [5], [4]]
# def bfs(start, graph, visited):
#         queue = deque([start])
#         visited[start] = 1 #1번 컴퓨터부터 시작이니까 1번 방문 표시
#         # 1, 3, 5, 2, 6
#         while queue: #큐가 비어있지 않으면 계속 반복
#             node = queue.popleft() # 큐에서 가장 왼쪽 노드를 꺼내서 값을 저장한다.  
#             for neighbor in graph[node]: #현재 노드의 모든 이웃 노드를 탐색
#                 if visited[neighbor]==0:
#                     queue.append(neighbor)
#                     visited[neighbor] = 1  
#         return sum(visited) -1

# C = int(input().strip()) #컴퓨터의 수
# N = int(input().strip()) #네트워크 상으로 연결된 컴퓨터 쌍의 수

# graph = [[] for _ in range(C+1)] #컴퓨터의 수보다 +1 많게 그래프 생성 
# # 만약 C가 4라면 graph 초기화는 [[],[],[],[],[]] 이다.
# for _ in range(N):
#     a, b= map(int, input().strip().split())
#     graph[a].append(b)
#     graph[b].append(a) #각각 해당 그래프의 인덱스에 뭐가 연결되어있는지 나타낸다.
# visited = [0] * (C+1) #방문기록 초기화 C+1하는 이유는 graph가 c+1개의 요소를 가지고 있으니까

# print(bfs(1,graph,visited)) #1번 컴퓨터를 제외하고 출력


import sys
from collections import deque

input =  sys.stdin.readline

def dfs(index):
    visited[index] = 1
    for neighbor in graph[index]:
        if visited[neighbor]==0:
            dfs(neighbor)
    return sum(visited)-1

C =  int(input().strip())
N = int(input().strip())
graph = [[] for _ in range(C+1)]
visited = [0]*(C+1)
for _ in range(N):
    a,b = map(int, input().strip().split())
    graph[a]+=[b]
    graph[b] +=[a]
print(dfs(1))