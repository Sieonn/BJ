# 두 수를 더하는 람다 함수를 작성하시오.
z = lambda x, y : x+y
x = 3
y = 4
print("1번",z(x, y))


# 리스트의 각 원소를 제곱하는 람다 함수를 작성하시오. 리스트 [1, 2, 3, 4]를 예로 들어보세요.

Nlist = [1, 2, 3, 4]
Z=list(map(lambda x : x**2, Nlist))
print("2번",Z)
# 문자열이 길이 5보다 긴지 확인하는 람다 함수를 작성하시오.

long_string = lambda s: len(s) > 5
print("3번",long_string("ASDWWW"))

# 두 수 중 큰 수를 반환하는 람다 함수를 작성하시오.
maxNum = lambda x, y : max(x, y)
print("4번",maxNum(5,6))

# 리스트에서 홀수만 필터링하는 람다 함수를 작성하시오. 리스트 [1, 2, 3, 4, 5, 6]를 예로 들어보세요.
N = [1, 2,3, 4, 5, 6]
# list(filter(lambda x: x % 2 != 0, N))
e =  list(filter(lambda x : x%2 != 0, N))
print("5번", e)
# 주어진 리스트의 모든 문자열을 대문자로 변환하는 람다 함수를 작성하시오. 리스트 ['apple', 'banana', 'cherry']를 예로 들어보세요.
N = ['apple', 'banana', 'cherry']
e = list(map(lambda x : x.upper() , N))
# "D".capitalize
print("6번", e)

# 주어진 리스트에서 10보다 큰 수의 개수를 세는 람다 함수를 작성하시오. 리스트 [5, 10, 15, 20, 25]를 예로 들어보세요.

N  = [5, 10, 15, 20, 25]
e = len(list(filter(lambda x : x > 10, N)))
print("7번", e)

# 두 문자열을 결합하는 람다 함수를 작성하시오.
A = "asdf"
B = "fdsa"
e = lambda x,y: x+y
print("8번",e(A, B))

# 주어진 문자열이 회문인지 확인하는 람다 함수를 작성하시오. (회문: 앞뒤가 같은 문자열, 예: 'radar')

A = "radar"
e = lambda x : x==x[:-1] 
print("9번",e(A))
# 주어진 리스트에서 각 원소에 3을 더한 결과를 반환하는 람다 함수를 작성하시오. 리스트 [1, 2, 3]을 예로 들어보세요.

N = [1, 2, 3]
e = list(map(lambda x : x+3, N))
print("10번",e)

