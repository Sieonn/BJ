import sys
input = sys.stdin.readline
from collections import deque


N = int(input().strip()) #사람수 입력
A, B = map(int, input().strip().split()) #찾을 두 수 입력
M  = int(input().strip()) #부모자식 관계 몇 쌍 보여줄건지 입력
family = [[] for _ in range(N+1)] # 계산하기 편하라고 +1을해서 인덱스를 활용
visited = [0]*(N+1)
result = []

for _ in range (M): #family그래프 생성
    x, y = map(int, input().strip().split())
    family[x].append(y)
    family[y].append(x)
    
#dfs
def dfs(v, num): # num은 재귀가 깊어지면(촌수를 이동할 때) +1을 해주었다.
    #v는 내가 현재 위치하고 있는 노드이다.
    num+=1 
    visited[v] = 1
    
    if v == B:
        return result.append(num)
        
    for i in family[v]:
        if visited[i]==0:
            dfs(i, num)
dfs(A, 0)
if len(result)==0:
    print(-1)
else:
    print(result[0]-1)