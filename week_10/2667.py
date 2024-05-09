import sys
input = sys.stdin.readline
from collections import deque
n = int(input())
graph = [list(map(int, input().strip())) for _ in range(n)]
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

def bfs(x, y):
    global graph
    queue = deque()
    queue.append((x, y))
    home = 1
    while queue:
        i, j = queue.popleft()
        for k in range(4):
            nx = i + dx[k]
            ny = j + dy[k]
            if 0 <= nx < n and 0 <= ny < n:
                if graph[nx][ny] == 1:
                    graph[nx][ny] = 0
                    home += 1
                    queue.append((nx, ny))
                    
    return home


town = 0
home_arr = []
for i in range(n):
    for j in range(n):
        if graph[i][j] == 1:
            town += 1
            graph[i][j] = 0
            home_arr.append(bfs(i,j))
print(town)
home_arr.sort()
for i in home_arr:
    print(i)