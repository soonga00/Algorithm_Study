import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**5)
def dfs(node):
    visited[node] = True
    for i in tree[node]:
        if not visited[i]:
            parent[i] = node
            dfs(i)

n = int(input())
parent = [0] * (n+1)
tree = [[] for _ in range(n+1)]
visited = [False] * (n+1)

for _ in range(n-1):
    p, c = map(int, input().split())
    tree[p].append(c)
    tree[c].append(p)

dfs(1)
for i in range(2, n+1):
    print(parent[i])