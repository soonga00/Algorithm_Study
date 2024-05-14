import sys
input = sys.stdin.readline

n = int(input())
graph = [list(map(int, input().split())) for _ in range(n)]

dx = [1, 0]
dy = [0, 1]
visited = [[False for _ in range(n)] for _ in range(n)]
def dfs(x, y, visited):
    move = graph[x][y]
    if move == -1:
        return True
    for i in range(2):
        nx = x + dx[i] * move
        ny = y + dy[i] * move
        if 0 <= nx < n and 0 <= ny < n:
            if not visited[nx][ny]:
                visited[nx][ny] = True
                if dfs(nx, ny, visited):
                    return True
                visited[nx][ny] = False
    return False
visited[0][0] = True
if dfs(0, 0, visited):
    print("HaruHaru")
else:
    print("Hing")
    