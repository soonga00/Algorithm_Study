import sys
input = sys.stdin.readline

def binary_search(target, start, end):
    while start <= end:
        mid = (start + end) // 2
        if arr[mid] == target:
            return True
        elif arr[mid] > target:
            end = mid - 1
        else:
            start = mid + 1
    return False


n = int(input())
arr = list(map(int, input().split()))
arr.sort()
m = int(input())
arr2 = list(map(int, input().split()))

for i in arr2:
    if binary_search(i, 0, n-1):
        print(1)
    else:
        print(0)