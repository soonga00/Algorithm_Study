import sys
input = sys.stdin.readline

def binary_search(start, end):
    while start <= end:
        mid = (start + end) // 2
        tmp = 0
        for i in tree:
            if i > mid:
                tmp += i - mid
        if tmp >= m:
            start = mid + 1
        else:
            end  = mid -1
    print(end)
            

n, m = map(int, input().split())
tree = list(map(int, input().split()))
tree.sort()
binary_search(1, max(tree))