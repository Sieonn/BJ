N = input()
Narr = sorted(list(map(int, input().split())))
# print(type(Narr), Narr)
M = int(input()) # 총 예산
v = M//len(Narr) #예산 평균
b = []
if sum(Narr) < M: 
    b.append(Narr[-1])
else:
    for i,j in enumerate(Narr):
        if v > j:
            M-=j
            b.append(j)
        else:
            v = M//(len(Narr)-i)
            b.append(v)
            break
        # print(v)
sorted(b)
print(b[-1])
