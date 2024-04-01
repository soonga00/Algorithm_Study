def get_max_sum(arr):
    global summation
    for i in range(0, len(arr), 2):
        if i+1 >= len(arr):
            summation += arr[i]
        else:
            if arr[i] == 1 or arr[i+1] == 1:
                summation += (arr[i] + arr[i+1])
            else:
                summation += (arr[i] * arr[i+1])
            
N = int(input())
pos = []
neg = []
for _ in range(N):
    num = int(input())
    if num > 0:
        pos.append(num)
    else:
        neg.append(num)

pos.sort(reverse=True)
neg.sort()

summation = 0

get_max_sum(pos)
get_max_sum(neg)

print(summation)