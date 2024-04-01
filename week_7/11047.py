import sys
n, k = map(int, input().split())
coin = []
for _ in range(n):
    coin.append(int(input()))
coin.sort(reverse=True)
min_cnt = 0
for i in range(n):
    if k >= coin[i]:
        min_cnt += (k // coin[i])
        k %= coin[i]
print(min_cnt)