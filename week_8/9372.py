import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    n, m = map(int, input().split())
    arr = []
    for i in range(m):
        arr.append(list(map(int, input().split())))
    print(n-1)

# 모든 엣지의 가중치가 1인 minimum spanning tree 는 node개수 - 1