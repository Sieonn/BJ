N, C = map(int,input().split())
# print(N, C)
numArr = list(map(int, input().split()))
rdic = {}
for _ in numArr:
    rdic[_] = numArr.count(_)
rdic= dict(sorted(rdic.items(),key=lambda item: (item[1], item[0]),reverse=True))
s = int(next(iter(rdic)))* rdic.values(rdic[0])
print(rdic, s)