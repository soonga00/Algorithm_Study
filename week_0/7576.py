from collections import deque

m,n = map(int, input().split())
box = [list(map(int, input().split())) for _ in range(n)]
queue = deque([])
day = 0
dx, dy = [1, 0, -1, 0], [0, 1, 0, -1]

for i in range(n):
    for j in range(m):
        if box[i][j] == 1:
            queue.append([i, j])
def bfs():
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx >= 0 and nx < n and ny >= 0 and ny < m and box[nx][ny] == 0:
                box[nx][ny] = box[x][y] + 1
                queue.append([nx, ny])

bfs()

for i in range(n):
    for j in range(m):
        if box[i][j] == 0:
            print(-1)
            exit(0)
        day = max(box[i][j], day)
print(day - 1)

    