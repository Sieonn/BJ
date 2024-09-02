# def sportsClass(n, lost, reserve):
#     count = n - len(lost)
#     for i in lost:
#         for j in reserve:
#             if i+1 in reserve or i-1 in reserve:
#                 count+=1
#             break
#     return count
def solution(n, lost, reserve):
    # 여벌이 있지만 도난당한 학생을 제외
    reserve_only = set(reserve) - set(lost)
    lost_only = set(lost) - set(reserve)
    
    # 빌려줄 수 있는 학생의 번호를 기준으로 정렬하며 lost 리스트를 순회
    for r in reserve_only:
        if r - 1 in lost_only:
            lost_only.remove(r - 1)
        elif r + 1 in lost_only:
            lost_only.remove(r + 1)
    
    # 전체 학생 수에서 체육복을 잃어버리고 빌리지 못한 학생 수를 뺀 값 반환
    return n - len(lost_only)
n=5
lost = [2, 4]
reserve = [1, 3, 5]
print(solution(n, lost, reserve))  # 출력: 5

