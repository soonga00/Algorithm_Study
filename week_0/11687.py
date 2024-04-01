def find_num_zero(n):
    result = 0
    while n >= 5:
        result += n//5
        n //= 5
    return result

m = int(input())

left, right, result = 1, m*5, 0

while left <= right:
    mid = (left + right) // 2

    if  find_num_zero(mid) < m:
        left = mid + 1
    else:
        right = mid - 1
        result = mid

if find_num_zero(result) == m:
    print(result)
else:
    print(-1)