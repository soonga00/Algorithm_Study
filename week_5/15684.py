def check():
    for col in range(n):
        line = col
        for row in range(h):
            if dp[row][line] == 1:
                line += 1
            elif line > 0 and dp[row][line-1] == 1:
                line -= 1
        if line != col:
            return False
    return True

def dfs(cnt, row, col):
    global min_cnt
    if check():
        min_cnt = min(min_cnt, cnt)
        return
    elif cnt == 3 or min_cnt <= cnt:
        return
    
    for i in range(row, h):
        if i == row:
            line = col
        else:
            line = 0
        for j in range(line, n-1):
            if dp[i][j] != 1 and dp[i][j+1] != 1:
                if j > 0 and dp[i][j-1] == 1:
                    continue
                dp[i][j] = 1
                dfs(cnt+1, i, j+2)
                dp[i][j] = 0

n, m, h = map(int, input().split())
dp = [[0 for _ in range(n)] for i in range(h)]
for _ in range(m):
    a, b = map(int, input().split())
    dp[a-1][b-1] = 1

min_cnt = 4
dfs(0, 0, 0)
print(min_cnt if min_cnt < 4 else -1)