import sys
input = sys.stdin.readline
from collections import deque
import copy

def bfs():
    queue = deque()
    queue.append((0, 0, 0))

    while queue:
        x, y, z = queue.popleft()
        if x == n - 1 and y == m - 1:
            return visited[x][y][z]
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or nx >= n or ny < 0 or ny >= m:
                continue
            if graph[nx][ny] == 1 and z == 0:
                visited[nx][ny][1] = visited[x][y][0] + 1
                queue.append((nx, ny, 1))
            if graph[nx][ny] == 0 and visited[nx][ny][z] == 0:
                visited[nx][ny][z] = visited[x][y][z] + 1
                queue.append((nx, ny, z))

    return -1

n,m = map(int, input().split())
graph = []
for _ in range(n):
    graph.append(list(map(int, input().strip())))

visited = [[[0, 0] for _ in range(m)] for _ in range(n)]
visited[0][0][0] = 1
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

print(bfs())