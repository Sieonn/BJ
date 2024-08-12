def solution(n, computers): #DFS사용
    answer = 0
    visited = [False for i in range(n)]
    
    def dfs(n, computers, i, visited): #n노드수, computers: 연결 상태, i:현재 인덱스, visited: 방문여부
        visited[i] = True #해당 인덱스 방문처리
        for j in range(n):
            if j != i and computers[i][j] == 1: #연결된 컴퓨터
                if visited[j] == False:
                    dfs(n, computers, j, visited)
                    
    for i in range(n):
        if visited[i] == False:
            dfs(n, computers, i , visited)
            answer += 1 #DFS로 최대한 컴퓨터들을 방문하고 빠져나오게 되면 그것이 하나의 네트워크.
        return answer

print(solution())