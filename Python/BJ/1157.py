# A = input()
# result ={}
# for i in A:
#     i=i.capitalize()
#     result[i] = result.get(i, 0) + 1

# max_value = max(result.values())
# max_keys = [k for k, v in result.items() if v == max_value]

# # 가장 큰 값이 여러 개라면 '?' 출력, 그렇지 않으면 해당 키 출력
# if len(max_keys) > 1:
#     print('?')
# else:
#     print(max_keys[0])


A = input()
result={}

for i in A:
    i = i.upper()
    result[i]= result.get(i,0) +1
maxValue=max(result.values())
maxKey = [k for k, v in result.items() if v == maxValue]

if len(maxKey)>1:
    print("?")
else:
    print(maxKey[0])