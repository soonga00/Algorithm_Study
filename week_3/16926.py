N, M, R = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]

for _ in range(R):
    for i in range(min(N, M) // 2):
        x, y = i, i
        tmp = arr[x][y]

        for j in range(i + 1, N - i):
            x = j
            now = arr[x][y]
            arr[x][y] = tmp
            tmp = now

        for j in range(i + 1, M - i):
            y = j
            now = arr[x][y]
            arr[x][y] = tmp
            tmp = now
        
        for j in range(N - i - 2, i - 1, -1):
            x = j
            now = arr[x][y]
            arr[x][y] = tmp
            tmp = now

        for j in range(M - i - 2, i - 1, -1):
            y = j
            now = arr[x][y]
            arr[x][y] = tmp
            tmp = now

for i in range(N):
    for j in range(M):
        if j != M - 1:
            print(arr[i][j], end=' ')
        else:
            print(arr[i][j])
