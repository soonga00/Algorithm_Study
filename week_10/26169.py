import sys
input = sys.stdin.readline

graph = [list(map(int, input().split())) for _ in range(5)]
r, c = map(int, input().split())
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]
result = 0
def dfs(graph, move, x, y, apple):
    global result
    if move == 3 and apple < 2:
        return
    if apple >= 2:
        result = 1
        return
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < 5 and 0 <= ny < 5:
            if graph[nx][ny] != -1:
                n_apple = graph[nx][ny]
                graph[nx][ny] = -1
                dfs(graph, move + 1, nx, ny, apple + n_apple)
                graph[nx][ny] = n_apple
graph[r][c] = -1
dfs(graph, 0, r, c, 0)
print(result)