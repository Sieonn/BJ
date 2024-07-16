N, C = map(int,input().split())
# print(N, C)
numArr = list(map(int, input().split()))
rdic = {}
for _ in numArr:
    rdic[_] = numArr.count(_)
rdic= dict(sorted(rdic.items(),
            key=lambda item: item[1],reverse=True))
s = []
for k,v in rdic.items():
    for i in range(v):
        s.append(k)   
print(*s)