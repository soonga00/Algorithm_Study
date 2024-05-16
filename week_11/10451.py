import sys
input = sys.stdin.readline

t = int(input())

def dfs(i):
    global cnt
    visited[i] = True
    if visited[arr[i]]:
        cnt += 1
        return
    else:
        dfs(arr[i])


for _ in range(t):
    n = int(input())
    arr = [0] + list(map(int, input().split()))
    visited = [False for _ in range(n+1)]
    cnt = 0
    for i in range(1,n+1):
        if not visited[i]:
            dfs(i)
    print(cnt)
