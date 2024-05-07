import sys
input = sys.stdin.readline
from collections import deque

def dfs(idx):
    visited[idx] = 1
    print(idx, end=" ")
    for i in adj[idx]:
        if visited[i] != 0:
            continue
        dfs(i)
    return

def bfs(idx):
    queue = deque()
    queue.append(idx)
    while queue:
        value = queue.popleft()
        if visited[value] == 0:
            print(value, end=" ")
            visited[value] = 1
            for i in adj[value]:
                queue.append(i)


n, m, v = map(int, input().split())
adj = [[] for _ in range(n+1)]

for _ in range(m):
    x, y = map(int, input().split())
    adj[x].append(y)
    adj[y].append(x)
for i in range(1, n+1):
    adj[i].sort()
visited = [0] * (n+1)
dfs(v)
print("")
visited = [0] * (n+1)
bfs(v)
print()