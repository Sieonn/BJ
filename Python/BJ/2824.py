import sys
import math
input = sys.stdin.readline

def gcd(A, B):
    while B !=0:
        A, B = B, A%B
    if(len(str(A)) >9):    
        return str(A)[-9:]
    else:
        return A

N = int(input())
A = math.prod(list(map(int, input().split())))
M = int(input())
B = math.prod(list(map(int, input().split())))
print(gcd(A, B))