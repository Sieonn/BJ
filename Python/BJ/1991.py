import sys
input = sys.stdin.readline

N = int(input().strip()) #이진트리의 노드의 개수

tree = {}
for i in N:
    root, left, right =map(str, input().strip().split())
    tree[root] = left,right
    
