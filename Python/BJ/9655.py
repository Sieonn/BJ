def stone_game(n):
    # 홀수면 상근이가 이김, 짝수면 창영이가 이김
    if n % 2 == 1:
        return "SK"
    elif n == 0:
        return False
    else:
        return "CY"

n = int(input())
print(stone_game(n))