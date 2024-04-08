import sys
sys.setrecursionlimit(10 ** 9)
input = sys.stdin.readline

n = int(input())
adj = [[] for _ in range(n+1)]
for _ in range(n-1):
    p, c = map(int, input().split())
    adj[p].append(c)
    adj[c].append(p)
visited = [-1]*(n+1)
dp = [[0, 1] for _ in range(n+1)]

def dfs(v):
    visited[v] = 1
    for c in adj[v]:
        if visited[c] == 1:
            continue
        dfs(c)
        dp[v][0] += dp[c][1]
        dp[v][1] += min(dp[c])
dfs(1)
print(min(dp[1]))