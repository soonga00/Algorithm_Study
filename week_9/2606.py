import sys
input = sys.stdin.readline

n = int(input())
pair_num = int(input())
graph = [[] for _ in range(n+1)]
visited = [0] * (n+1)
cnt = 0
for _ in range(pair_num):
    x, y = map(int, input().split())
    graph[x].append(y)
    graph[y].append(x)

def dfs(idx):
    global cnt
    visited[idx] = 1
    for i in graph[idx]:
        if visited[i] != 0:
            continue
        cnt += 1
        dfs(i)
    return
dfs(1)
print(cnt)