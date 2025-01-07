def solution(keyinput, board):
    start = [0,0]
    for i in keyinput:
        if i == "up" and abs(start[1]) <= board[1]//2:
            start[1] += 1
            if abs(start[1]) > board[1]//2:
                start[1] -= 1 
        elif i == "down" and  abs(start[1]) <= board[1]//2:
            start[1] -= 1
            if abs(start[1]) > board[1]//2:
                start[1] += 1 
        elif i == "right" and abs(start[0]) <= board[0]//2:
            start[0] += 1
            if abs(start[0]) > board[0]//2:
                start[0] -= 1
        elif i == "left" and abs(start[0]) <= board[0]//2:
            start[0] -= 1
            if abs(start[0]) > board[0]//2:
                start[0] += 1
    return start