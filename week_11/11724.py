import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**5)

def dfs(i):
    global visited
    for j in graph[i]:
        if not visited[j]:
            visited[j] = True
            dfs(j)
n, m = map(int, input().split())
graph = [[] for _ in range(n+1)]

for _ in range(m):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)
visited = [False for _ in range(n+1)]
cnt = 0
for i in range(1, n+1):
    if not visited[i]:
        visited[i] = True
        dfs(i)
        cnt +=1
print(cnt)
