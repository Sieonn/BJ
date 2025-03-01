chess = [1,1,2,2,2,8]
n = list(map(int, input().split()))
result=[]
for i in range(len(n)):
    val = chess[i] - n[i]
    result.append(val)
print(*result)