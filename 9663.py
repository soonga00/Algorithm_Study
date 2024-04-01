n = int(input())
queen = [0 for _ in range(n)]
cnt = 0

def is_possible(x):
    for i in range(x):
        if queen[x] == queen[i] or abs(queen[x] - queen[i]) == abs(x-i):
            return False
    return True

def n_queen(x):
    global cnt
    if x == n:
        cnt +=1
        return
    
    for y in range(n):
        queen[x] = y
        if is_possible(x):
            n_queen(x+1)
n_queen(0)
print(cnt)