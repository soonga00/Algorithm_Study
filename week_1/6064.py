def find_year(M, N, x, y):
    while x <= M*N:
        if (x - y) % N == 0:
            return x
        x += M
    return -1


n = int(input())

for _ in range(n):
    M, N, x, y = map(int, input().split())
    year = 1
    print(find_year(M, N, x, y))
