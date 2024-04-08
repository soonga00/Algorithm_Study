n = int(input())
arr = list(map(int, input().split()))
delete_value = int(input())

def dfs(node):
    arr[node] = -10
    for i in range(n):
        if arr[i] == node:
            dfs(i)
dfs(delete_value)
cnt = 0
for i in range(n):
    if arr[i] != -10 and i not in arr:
        cnt += 1
print(cnt)