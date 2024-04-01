import sys
n = int(input())
distance = list(map(int, input().split()))
oil = list(map(int, input().split()))
min_price = oil[0]
result = 0

for i in range(n-1):
    if min_price > oil[i]:
        min_price = oil[i]
    result += (min_price*distance[i])
print(result)
