# 문자열 my_string이 매개변수로 주어집니다. my_string에서 중복된 문자를 제거하고 
# 하나의 문자만 남긴 문자열을 return하도록 solution 함수를 완성해주세요.

#1.값을 받고 만약 있으면 넣지 않고 없으면 넣는다.
def solution(my_string):
    result = []
    for i in my_string:
        if i not in result:
            result.append(i)
    return "".join(result)
print(solution("We are the world"))
