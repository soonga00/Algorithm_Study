import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**5)
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

def dfs(x, y):
    global graph
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < m and 0 <= ny < n:
            if graph[nx][ny] == 1:
                graph[nx][ny] = 0
                dfs(nx, ny)
            


t = int(input())
for _ in range(t):
    m, n, k = map(int, input().split())
    cnt = 0
    graph = [[0 for _ in range(n)] for _ in range(m)]
    for _ in range(k):
        x, y = map(int, input().split())
        graph[x][y] = 1
    for i in range(m):
        for j in range(n):
            if graph[i][j] == 1:
                graph[i][j] = 0
                dfs(i, j)
                cnt += 1
    print(cnt)