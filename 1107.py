n = int(input())
m = int(input())
if m:
    broken_btn = list(map(int, input().split()))
else:
    broken_btn = []

min_cnt = abs(n-100)

for i in range(1000001):
    num = str(i)
    for j in range(len(num)):
        if int(num[j]) in broken_btn:
            break
        elif j == len(num)-1:
            min_cnt = min(min_cnt, len(num) + abs(n-i))
print(min_cnt)