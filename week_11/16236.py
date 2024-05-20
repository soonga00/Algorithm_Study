import sys
input = sys.stdin.readline
from collections import deque
n = int(input())
graph = [list(map(int, input().split())) for _ in range(n)]
babyshark_size = 2
babyshark_eat_num = 0

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]
def bfs(i, j, c):
    queue = deque()
    visited = [[False for _ in range(n)] for _ in range(n)]
    queue.append((i, j, c))
    fishes = []
    while queue:
        x, y, cnt = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < n and not visited[nx][ny]:
                if 0 < graph[nx][ny] < babyshark_size:
                    fishes.append((nx, ny, cnt+1))
                if graph[nx][ny] <= babyshark_size:
                    visited[nx][ny] = True
                    queue.append((nx, ny, cnt+1))

    return sorted(fishes, key = lambda x :(x[2], x[0], x[1]))

pos = []
for i in range(n):
        for j in range(n):
            if graph[i][j] == 9:
                 pos.append(i)
                 pos.append(j)
time = 0
i, j = pos
while 1:
    graph[i][j] = babyshark_size
    fishes = deque(bfs(i, j, 0))

    if not fishes:
        break
    x, y, cnt = fishes.popleft()
    time += cnt
    babyshark_eat_num += 1
    if babyshark_eat_num == babyshark_size:
        babyshark_size += 1
        babyshark_eat_num = 0
    graph[i][j] = 0
    i, j = x, y
    
    
print(time)
    
