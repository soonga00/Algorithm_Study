m, n = map(int, input().split())
map_list = [list(map(int, input().split())) for _ in range(m)]
dp = [[-1] * n for _ in range(m)]
dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]
dp[m-1][n-1] = 1

def dfs(x, y):
    if dp[x][y] != -1:
        return dp[x][y]
    
    cnt = 0
    for d in range(4):
        nx, ny = x + dx[d], y + dy[d]
        if 0 <= nx < m and 0<= ny < n:
            if map_list[nx][ny] < map_list[x][y]:
                cnt += dfs(nx, ny)
    dp[x][y] = cnt
    return dp[x][y]

print(dfs(0, 0))