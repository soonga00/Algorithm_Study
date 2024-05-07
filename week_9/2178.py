import sys
input = sys.stdin.readline
from collections import deque

d = [[1,0], [0, 1], [-1, 0], [0, -1]]

n, m = map(int, input().split())
graph = []
for _ in range(n):
    graph.append(list(map(int, input().strip())))

def dfs(x, y):
    queue = deque()
    queue.append((x, y))
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            dx = x + d[i][0]
            dy = y + d[i][1]
            if 0 <= dx < n and 0 <= dy < m and graph[dx][dy] == 1:
                queue.append((dx, dy))
                graph[dx][dy] = graph[x][y] + 1
    return graph[n-1][m-1]

print(dfs(0, 0))
    