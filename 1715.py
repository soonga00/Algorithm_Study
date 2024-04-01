import heapq
import sys
input = sys.stdin.readline

card = []
n = int(input())
for _ in range(n):
    heapq.heappush(card, int(input()))
cnt = 0
while len(card) != 1:
    a = heapq.heappop(card)
    b = heapq.heappop(card)
    heapq.heappush(card, a+b)
    cnt += a+b

print(cnt)