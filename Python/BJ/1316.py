#그룹 단어란 단어에 존재하는 모든 문자에 대해서, 각 문자가 연속해서 나타나는 경우만을 말한다. 예를 들면, ccazzzzbb는 c, a, z, b가 모두 연속해서 나타나고, kin도 k, i, n이 연속해서 나타나기 때문에 그룹 단어이지만, aabbbccb는 b가 떨어져서 나타나기 때문에 그룹 단어가 아니다.
# 단어 N개를 입력으로 받아 그룹 단어의 개수를 출력하는 프로그램을 작성하시오.

# 3
# happy
# new
# year
from collections import OrderedDict
n = input()
wordList = [input() for _ in range(int(3))]
wordList2 = [list(OrderedDict.fromkeys(input())) for _ in range(int(3))]

print(wordList)
for i in wordList2:
    for j in i:
        for K in 
        
result = []

for i in wordList:
    for j in i:
        
        