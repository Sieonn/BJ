def palindrome(s):
    return s == s[::-1]
def min_palindrome(s):
    for i in range(len(s)):
       if palindrome(s[i:]): #만약 해당 문자열이 팰린드롬이라면
           return len(s) + i #i는 문자열을 탐색하기 시작하는 인덱스여서 팰린드롬으로 판명된 문자열을 제외한 앞 문자의 길이를 판단한다.
    return 2* len(s) - 1 #가장 끝 문자열을 기준으로
#팰린드롬이 생성됐다고 생각하면된다.

# abcd
s = input();
print(min_palindrome(s))
