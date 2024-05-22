import sys, math
input = sys.stdin.readline

x, y = map(int, input().split())

left, right = 1, x
z = math.floor(y * 100 / x)
ans = 1000000001
while (left <= right):
    mid = (left+right) // 2
    tmp = math.floor((y + mid) * 100 /(x + mid))
    if tmp > z:
        right = mid - 1
        ans = mid
    else:
        left = mid + 1
if ans == 1000000001:
    print(-1)
else:
    print(ans)