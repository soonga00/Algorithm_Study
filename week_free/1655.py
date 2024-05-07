import sys
import heapq
input = sys.stdin.readline

n = int(input())
left_heap = []
right_heap = []
for i in range(n):
    num = int(input())
    if len(left_heap) == len(right_heap):
        heapq.heappush(left_heap, -num)
    else:
        heapq.heappush(right_heap, num)
    if right_heap and right_heap[0] < -left_heap[0]:
        left_value = heapq.heappop(left_heap)
        right_value = heapq.heappop(right_heap)
        heapq.heappush(left_heap, -right_value)
        heapq.heappush(right_heap, -left_value)
    print(-left_heap[0])