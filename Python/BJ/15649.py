# 자연수 N과 M이 주어졌을 때, 아래 조건을 만족하는 길이가 M인 수열을 모두 구하는 프로그램을 작성
# 1부터 N까지 자연수 중에서 중복 없이 M개를 고른 수열

def dfs():
    if len(a)==M: # 리스트의 길이가 M과 같아지면  배열을 출력하고 함수를 호출한 곳으로 다시 돌아가도록 합니다.
        print(' '.join(map(str,a)))
        return
    for i in range(1,N+1):# 같지 않으면 1에서 N+1까지의 for문을 실행합니다.
        if visited[i]: #호출한 인덱스를 방문했다면 넘어갑니다.
            continue
        visited[i] = True # 방문하지 않았다면 방문처리해놓습니다.
        a.append(i) #그 인덱스를 a에 담고 함수를 다시 호출합니다. 
        dfs() # 여기서 if의 조건을 만족한다면 return 후 다시 돌아와pop을 실행한다.
        a.pop()
        visited[i] =False # 꺼내고 나서는 해당 인덱스는 다시 방문하지 않은 것으로 처리합니다. 

N, M = map(int, input().split()) #N과 M을 입력받습니다.
a = [] #수열을 담을 빈 리스트 
visited = [False]*(N+1) #해당 수를 방문했는지 여부로 중복 없이 가져올 수 있습니다.
dfs()