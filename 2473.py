N = int(input())
arr = list(map(int, input().split()))
arr.sort()

left, mid ,right = 0, 1, N-1
result = abs(arr[left]+arr[mid]+arr[right])
min_idx, mid_idx, max_idx = 0, 1, N-1
for i in range(N-2):
    left = i
    mid = left + 1
    right = N-1
    while mid < right:
        summation = arr[left]+arr[mid]+arr[right]
        if abs(summation) < result:
            result = abs(summation)
            min_idx = left
            mid_idx = mid
            max_idx = right
            if result == 0:
                break
        if summation < 0:
            mid += 1
        else:
            right -=1

print(arr[min_idx], arr[mid_idx], arr[max_idx])