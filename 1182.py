def dfs(start, tmp, s):
    global cnt
    if sum(tmp) == s and len(tmp) > 0:
        cnt += 1
        # print("cnt = ", cnt, "tmp = ", tmp)
        # print()
    if start == n:
        return
    for i in range(start, n):
        tmp.append(arr[i])
        # print(i, "'s append : ", arr[i], " tmp = ", tmp)
        dfs(i+1, tmp, s)
        tmp.pop(-1)
        # print(i, "'s pop : ", tmp.pop(-1), " tmp = ", tmp)
n, s = map(int, input().split())

arr = list(map(int, input().split()))
cnt = 0
tmp = []
dfs(0, tmp,s)
print(cnt)