import sys
input = sys.stdin.readline

cnt = 0
n, m = map(int, input().split())
home = [list(map(str, input().strip())) for _ in range(n)]

def dfs(x, y):
    if home[x][y] == '-':
        home[x][y] = 1
        for j in [1, -1]:
            ny = y + j
            if (ny >= 0 and ny < m)  and home[x][ny] == '-':
                dfs(x, ny)
            elif ny == m:
                return
    if home[x][y] == '|':
        home[x][y] = 1
        for i in [1, -1]:
            nx = x + i
            if (nx >= 0 and nx < n)  and home[nx][y] == '|':
                dfs(nx, y)
            elif nx == n:
                return


for i in range(n):
    for j in range(m):
        if home[i][j] == '-' or home[i][j] == '|':
            dfs(i, j)
            cnt += 1
print(cnt)