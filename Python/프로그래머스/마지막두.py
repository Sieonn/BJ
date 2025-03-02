def solution(num_list):
    last = num_list[-1]
    pre_last = num_list[len(num_list)-2]
    print(last, pre_last)
    if last > pre_last:
        num_list.append(last - pre_last)
    else:
        num_list.append(last * 2)
    return num_list
print(solution([2, 1, 6]))