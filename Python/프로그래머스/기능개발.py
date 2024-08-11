# import math
# def solution(progresses, speeds):
#     rest = list(map(lambda x: 100-x,progresses)) #완료까지 남은 날짜
#     sol =[]
#     day = []
#     index =0
#     for i in range(0, len(progresses)):
#         day.append(math.ceil(rest[i]/speeds[i])) #며칠 걸리는지
#         if i==0:
#             sol.append(1)
#         elif day[i] < day[i-1] and i!=0:
#             sol[index] = sol[index]+1
#         elif day[i] > day[i-1] and i!=0:
#             index +=1
#             sol[index] =
#     print(sol)

# progresses =[93, 30, 55]
# speeds = [1, 30, 5]	
# solution(progresses,speeds)




# 처음에 진행도, 스피드 받는다.
# 그리고 걸릴 날짜를 구한다.
#새로운 곳에서 만약 걸릴 날짜가 이 전보다 작으면 +1 크면 인덱스를 추가해서 거기에 +1


# pro =[93, 30, 55]
# spe = [1, 30, 5]
# import math
# def sol(pro, spe):
#     pro = list(map(lambda x: 100-x ,pro)) #[7, 70, 45]
#     day = list(map(lambda x,y : math.ceil(x/y)  ,pro,spe)) #[7, 3, 9]
    
#     result = [1]
#     index = 0
#     for i in range(1, len(pro)):
#         if day[i]<day[i-1] or day[i]==day[i-1]:
#             result[index] = result[index]+1
#             # print(result)
#         else:
#             result.append(1)
#             index +=1
#     return result
import math
def solution(pro, spe):
    pro = list(map(lambda x: 100-x ,pro)) 
    day = list(map(lambda x,y : math.ceil(x/y) ,pro,spe)) 
    print(pro, day)#[1, 2] ,[1, 2]
    
    result = [1]
    index = 0
    for i in range(1, len(pro)):
        kigon = 0
        if day[i]<day[kigon] or day[i]==day[kigon]:
            result[index] = result[index]+1
        else:
            result.append(1)
            index +=1
            kigon = i
    return result
    
pro = [99, 98] #하루 뒤 [100, 99 ]
spe =   [1, 1]
print(solution(pro,spe))