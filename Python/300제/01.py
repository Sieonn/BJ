# print("Hello Wolrd")

A, P = map(int,input().strip().split())
result = [A]
start = str(A)
while len(result)>0:
    val=0
    for i in start:
        val += int(i)**P
    print(result)        
    if str(val) in result:
        B = result.index(str(val))
        print(len(result[:B]))
        break
    else:
        result.append(str(val))
        start = str(val)
