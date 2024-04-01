from itertools import permutations

n, d = map(int, input().split())
arr = []
for i in range(d):
    arr.insert(0, i)
permutation_arr = list(permutations(arr))
permutation_arr.sort()
for i in permutation_arr:
    num = 0
    for j in range(d):
        num += i[d-j-1] * (d**j)
    if num > n and i[0] != 0:
        print(num)
        exit()
print(-1)
