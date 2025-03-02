def solution(todo_list, finished):
    result = []
    for i, v in enumerate(finished):
        if v == False:
            result.append(todo_list[i])
    return result
print(solution(["problemsolving", "practiceguitar", "swim", "studygraph"], ['true', 'false', 'true', 'false']))