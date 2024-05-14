import sys
input = sys.stdin.readline
r, c = map(int, input().split())

graph = [list(map(str, input().strip())) for _ in range(r)]

max_len = 0
arr = set()
arr.add(graph[0][0])
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]
def dfs(x, y, cnt):
    global max_len
    max_len = max(max_len, cnt)
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < r and 0 <= ny < c and not graph[nx][ny] in arr:
               arr.add(graph[nx][ny])
               dfs(nx, ny, cnt+1)
               arr.remove(graph[nx][ny])
                        
dfs(0, 0, 1)
print(max_len)