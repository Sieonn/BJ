def palindrome(s):
    return s == s[::-1]
def min_palindrome(s):
    for i in range(len(s)):
        if palindrome(s[i:]):
            return len(s) + i
    return len(s)*2 - 1
s = input()
print(min_palindrome(s))