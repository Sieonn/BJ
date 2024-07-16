import sys
import bisect

input = sys.stdin.readline
tc = int(input().strip())

for _ in range(tc):
    A, B = map(int, input().strip().split())
    Aarr = list(map(int, input().strip().split()))
    Barr = sorted(list(map(int, input().strip().split())))
    
    count = 0
    for a in Aarr:
        # bisect_left를 사용하여 a보다 작은 요소의 개수를 찾음
        count += bisect.bisect_left(Barr, a)
    
    print(count)