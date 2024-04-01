N = int(input())
arr = list(map(int, input().split()))
arr.sort()

left, right = 0, N-1
result = abs(arr[left]+arr[right])
min_idx, max_idx = 0, N-1
while left < right:
    summation = arr[left]+arr[right]

    if abs(summation) < result:
        result = abs(summation)
        min_idx = left
        max_idx = right
        if result == 0:
            break
    if summation < 0:
        left += 1
    else:
        right -= 1
print(arr[min_idx], arr[max_idx])