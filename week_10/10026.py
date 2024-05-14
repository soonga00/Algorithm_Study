import sys, copy
input = sys.stdin.readline
from collections import deque

n = int(input())
graph = [list(map(str, input().strip())) for _ in range(n)]
cnt_normal = 0
cnt_not_normal = 0
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]
def bfs(graph, i, j, k, c):
    global cnt_normal
    global cnt_not_normal
    queue = deque()
    queue.append((i, j))

    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < n:
                if graph[nx][ny] == c:                  
                    graph[nx][ny] = '0'
                    queue.append((nx, ny))
                elif k == 1 and c != 'B'and graph[nx][ny] != 'B' and graph[nx][ny] != '0':
                    graph[nx][ny] = '0'
                    queue.append((nx, ny))
    if k == 0:
        cnt_normal += 1
    else:
        cnt_not_normal += 1



for k in range(2):
    tmp_graph = copy.deepcopy(graph)
    for i in range(n):
        for j in range(n):
            if tmp_graph[i][j] != '0':
                c = tmp_graph[i][j]
                tmp_graph[i][j] = '0'
                bfs(tmp_graph, i, j, k, c)
print(cnt_normal, cnt_not_normal)
