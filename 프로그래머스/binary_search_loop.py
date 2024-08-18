def binary_search(target, data):
    data.sort()
    start=0 #맨 처음 위치
    end =len(data)-1  # 맨 마지막 위치
    
    while start <= end:
        mid = (start +end) //2 #중간값
        
        if data[mid] ==target: 
            return mid #target위치 반환
        elif data[mid] > target: #target이 작으면 왼쪽을 더 탐색
            #전체 리스트에서 end가 줄어드니까  mid도 왼쪽으로 한칸 줄어든다.
            end = mid-1
        else: #target이 크면 오른쪽을 더 탐색
            start = mid + 1
    return   

print(binary_search(4, [1, 2, 3, 4, 5, 6, 7, 8, 9,12]))
#target의 위치인 3이 반환