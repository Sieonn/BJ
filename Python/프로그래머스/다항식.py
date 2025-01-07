def solution(polynomial):
    ploy = list(polynomial.split(" + "))
    #+ 양옆에 공백에 있다는 것을 유의의
    print(ploy)
    a = 0
    b = 0
    for i in ploy:
        if "x" in i:
            i = i.replace("x", "")
            if i == "":
                i = 1
            a += int(i)
        else:
            b += int(i)
            
    if a == 1:
        a = "x"
    elif a > 1:
        a = str(a)+ "x"
    else:
        return str(b)    
    if b == 0:
        return a
    else:
        return a + " + " + str(b)
    
print(solution("3x + x"))