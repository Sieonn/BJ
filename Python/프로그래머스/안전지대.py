# def find(board):
#     for i in range():
        
        

# def solution(board):
#     n = len(board[0])
#     count = [[False]* _ for _ in range(len(board[0]))]
#     for i in range(n):
#         for v in range(n): 
#             if board[i][v]
#             if count[i][v] != True:
#                 count[i][v] = True
        

# print(solution([[0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 1, 0, 0], [0, 0, 0, 0, 0]]))

# (x,y)
# (x-1,y)
# (x+1,y)
# (x-1,y+1)
# (x, y+1)
# (x+1, y+1)
# (x-1,y-1)
# (x, y-1)
# (x+1, y-1)

def findBoom(board):
    n = len(board[0])
    boom = []
    for i in range(n):
        for k in range(n):
            if board[i][k] == 1:
                boom.append([i,k])
    return boom
def soultion(board):
    boom = findBoom(board)
    round = []
    
    return boom


board = [[0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 1, 0, 0], [0, 0, 0, 0, 0]]
print(soultion(board))