N = int(input())
arr = list(map(int, input().split()))
arr.sort()
time = 0
tmp = 0
for i in range(N):
    time += tmp + arr[i]
    tmp += arr[i]
print(time)