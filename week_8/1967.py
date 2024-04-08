import sys

input = sys.stdin.readline
sys.setrecursionlimit(10**5)
n = int(input())
graph = [[] for _ in range(n+1)]

distance = [-1] * (n+1)
distance[1] = 0

for i in range(n-1):
    p, c, e = map(int, input().split())
    graph[p].append([c, e])
    graph[c].append([p, e])

def dfs(value, wei):
    for a, b in graph[value]:
        if distance[a] == -1:
            distance[a] = wei + b
            dfs(a, distance[a])
dfs(1, 0)

start = distance.index(max(distance))
distance = [-1] * (n+1)
distance[start] = 0
dfs(start, 0)

print(max(distance))
