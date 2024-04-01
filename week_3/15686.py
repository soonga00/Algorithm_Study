from itertools import combinations

N, M = map(int, input().split())
city = [list(map(int, input().split())) for _ in range(N)]
chicken_len = 2 * N * (2 * N - 2)
home = []
store = []

for i in range(N):
    for j in range(N):
        if city[i][j] == 1:
            home.append([i, j])
        elif city[i][j] == 2:
            store.append([i, j])

for s in combinations(store, M):
    tmp = 0
    for h in home:
        chi_len = 2 * N - 2
        for i in range(M):
            chi_len = min(chi_len, abs(s[i][0] - h[0]) + abs(s[i][1] - h[1]))
        tmp += chi_len
    chicken_len = min(chicken_len, tmp)

print(chicken_len)