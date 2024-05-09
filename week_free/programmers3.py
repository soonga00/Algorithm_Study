from collections import deque
m = 6
n = 4
picture = [[1, 1, 1, 0], [1, 2, 2, 0], [1, 0, 0, 1], [0, 0, 0, 1], [0, 0, 0, 3], [0, 0, 0, 3]]

num_of_area = 0
max_area = 0
dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]
        
def bfs(x, y):
    global num_of_area
    global max_area
    queue = deque()
    temp_area = 1
    queue.append((x, y, picture[x][y], temp_area))
    picture[x][y] = 0
    while queue:
        x, y, v, area = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0<=nx < m and 0 <= ny < n:
                if picture[nx][ny] == v:
                    temp_area += 1
                    queue.append((nx, ny, v, temp_area))
                    picture[nx][ny] = 0
    num_of_area += 1
    max_area = max(temp_area, max_area)

for i in range(m):
    for j in range(n):
        if picture[i][j] != 0:
            bfs(i, j)

print(num_of_area, max_area)