import sys
input = sys.stdin.readline

N,K =  input().split()

listA = list(map(int, input().strip().split()))
rcount = []
for i in range(0, int(N)-int(K)):
    count = 0
    new = []    
    for r, j in enumerate(listA[i:]):
        if j==1:
            count +=1
        # new.append(j)
        if count >= 3:
            new = listA[i:r]
            rcount.append(len(new))
print(sorted(rcount)[0])
            