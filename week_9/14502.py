import sys
from collections import deque
import copy
input = sys.stdin.readline

n,m = map(int, input().split())
map = [list(map(int, input().split())) for _ in range(n)]
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]
answer = 0
def bfs():
    queue = deque()
    temp_map = copy.deepcopy(map)

    for i in range(n):
        for j in range(m):
            if temp_map[i][j] == 2:
                queue.append((i, j))
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < n and 0 <= ny < m:
                if temp_map[nx][ny] == 0:
                    temp_map[nx][ny] = 2
                    queue.append((nx, ny))
    global answer
    cnt = 0

    for i in range(n):
        cnt += temp_map[i].count(0)
    answer = max(answer, cnt)

def dfs(wall):
    if wall == 3:
        bfs()
        return
    
    for i in range(n):
        for j in range(m):
            if map[i][j] == 0:
                map[i][j] = 1
                dfs(wall+1)
                map[i][j] = 0
dfs(0)
print(answer)
