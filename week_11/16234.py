import sys
input = sys.stdin.readline
from collections import deque
n, l, r = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]
queue = deque()
def bfs(i, j):
    queue.append((i, j))
    union = []
    union.append((i, j))
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < n and not visited[nx][ny]:
                if l <= abs(graph[x][y] - graph[nx][ny]) <= r:
                    visited[nx][ny] = True
                    queue.append((nx, ny))
                    union.append((nx, ny))
    if len(union) <= 1:
        return 0
    result = sum(graph[x][y] for x, y in union) // len(union)
    for x, y in union:
        graph[x][y] = result
    return 1
day = 0
while 1:
    stop = 0
    visited = [[False for _ in range(n)] for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if not visited[i][j]:
                visited[i][j] = True
                stop += bfs(i, j)
    if stop == 0:
        break
    day += 1
print(day)


    
