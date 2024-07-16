import sys 
input = sys.stdin.readline
n = int(input().strip())
arr = set()
for _ in range(n):
    str=input().strip().split()
    if str[1] == 'enter':
        arr.add(str[0])
    else:
        arr.remove(str[0])
arr=sorted(arr,reverse=True)
print(*arr, sep="\n")