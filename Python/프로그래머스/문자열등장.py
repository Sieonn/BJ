def solution(myString, pat):
    test = ""
    result = 0
    for i in range(0,len(myString)-len(pat)+1):
        test += myString[i: i+len(pat)]
        print(test)
        if test == pat:
            result +=1
        test=""
    return result

print(solution("banana", "ana"))