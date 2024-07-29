<<<<<<< HEAD
# import sys
# input = sys.stdin.readline

# N,K =  input().split()

# listA = list(map(int, input().strip().split()))
# rcount = []
# for i in range(0, int(N)-int(K)):
#     count = 0
#     new = []    
#     for j in listA[i:]:
#         if j==1:
#             count +=1
#         new.append(j)
#         if count >= 3:
#             rcount.append(len(new))
#             break;
# rcount.sort()
# print(rcount[0])
# 시간초과

def ryan(N, K, dolls):
    left = 0
    cnt_ryan = 0
    min_len = float('inf')

    for right in range(N):
        if dolls[right] ==1:
            cnt_ryan +=1
        while cnt_ryan >=K:
            min_len = min(min_len, right -left +1)
        if dolls[left] ==1:
            cnt_ryan -=1
        left+=1
    return-1 if min_len ==float('inf') else min_len

N, K = map(int, input().split())
dolls = list(map(int, input().split()))

print(ryan(N,K,dolls))
=======
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
            
>>>>>>> 72b3d19447feca5db286defb9cea01f401d2d795
