import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**5)

t = int(input())
group_num = 0
    

def dfs(i):
    global result
    visited[i] = True
    cycle.append(i)
    next = arr[i]
    if visited[next]:
        if next in cycle:
            result += cycle[cycle.index(next):]
        return
    else:
        dfs(next)


for _ in range(t):
    n = int(input())
    arr = [0] + list(map(int, input().split()))
    visited =[True] + [False] * n
    result = []

    for i in range(1, n+1):
        if not visited[i]:
            cycle = []
            dfs(i)
    print(n - len(result))