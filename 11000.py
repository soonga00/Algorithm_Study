import heapq
import sys
input = sys.stdin.readline

n = int(input())
q = [list(map(int, input().split())) for _ in range(n)]

q.sort()
classroom = []
heapq.heappush(classroom, q[0][1])

for i in range(1, n):
    if q[i][0] >= classroom[0]:
        heapq.heappop(classroom)
    heapq.heappush(classroom, q[i][1])
print(len(classroom))