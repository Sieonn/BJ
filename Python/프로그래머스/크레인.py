def solution(board, moves):
    stack = []
    count = 0
    
    for move in moves:
        col = move -1
        for row in range(len(board)):
            if board[row][col] != 0:
                doll =  board[row][col]
                board[row][col] = 0
                
                if stack and stack[-1] == doll:
                    stack.pop()
                    count += 2
                else: 
                    stack.append(doll)
                break
    return count

print(solution([[0,0,0,0,0],[0,0,1,0,3],[0,2,5,0,1],[4,2,4,4,2],[3,5,1,3,1]],[1,5,3,5,1,2,1,4]))