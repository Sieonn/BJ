def solution(s):
    a = []
    bracket_map = {')':'(', '}':'{', ']':'['}
    
    for char in s:
        if char in bracket_map.values():
            a.append(char)
        elif char in bracket_map.keys():
            if a == [] or a.pop() != bracket_map[char]:
                return False
    return not a
print(solution("((({{}})))"))