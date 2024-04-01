import sys
def dfs(total, i, add, sub, mult, div):
    global max_num
    global min_num
    if i == N:
        max_num = max(max_num, total)
        min_num = min(min_num, total)
        return
    
    if add:
        dfs(total + arr[i], i+1, add-1, sub, mult, div)
    if sub:
        dfs(total - arr[i], i+1, add, sub-1, mult, div)
    if mult:
        dfs(total * arr[i], i+1, add, sub, mult-1, div)
    if div:
        dfs(int(total / arr[i]), i+1, add, sub, mult, div-1)

N = int(input())
arr = list(map(int, input().split()))
op = list(map(int, input().split()))

tmp_op = []
max_num = -sys.maxsize
min_num = sys.maxsize

dfs(arr[0], 1, op[0], op[1], op[2], op[3])
print(max_num)
print(min_num)