# 걸그룹의수 N
#맞춰야할 문제수 M
# 사람 넣을곳이랑 그룹 넣을 리스트 두개 만들고
N, M = map(int, input().split())
arr = []
for i in range(N):
    arr.append([input()])
    S = int(input())
    for j in range(S):
        arr[i].append(input())

def findrow(arr, val):
    for index,v in enumerate(arr):
        for j in v:
            if val == j:
                return index
for i in range(M):
    val =  input()
    num= input()
    if num=="0":
        print(*sorted(arr[findrow(arr, val)][1:]), sep="\n")
    elif num=="1":
        print(arr[findrow(arr, val)][0])