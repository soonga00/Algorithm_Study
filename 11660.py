import sys 
input = sys.stdin.readline
n,m = map(int,input().split())
prefix_arr = [[0 for _ in range(n)] for _ in range(n)]
arr = []
for i in range(n):
    arr.append(list(map(int,input().split())))

for i in range(n*n):
    if i == 0:
        prefix_arr[0][0] = arr[0][0]
    elif i//n == 0:
        prefix_arr[0][i%n] = prefix_arr[0][i%n-1] + arr[0][i%n]
    elif i%n == 0:
        prefix_arr[i//n][0] = prefix_arr[i//n-1][0] + arr[i//n][0]
    else:
        prefix_arr[i//n][i%n] = prefix_arr[i//n][i%n-1] + prefix_arr[i//n-1][i%n] - prefix_arr[i//n-1][i%n-1] + arr[i//n][i%n]

for _ in range(m):
    x1,y1,x2,y2 = map(int,input().split())
    x1,y1,x2,y2 = x1-1,y1-1,x2-1,y2-1
    if x1 == 0 and y1 == 0:
        print(prefix_arr[x2][y2])
    elif x1 == 0:
        print(prefix_arr[x2][y2] - prefix_arr[x2][y1-1])
    elif y1 == 0:
        print(prefix_arr[x2][y2] - prefix_arr[x1-1][y2])
    else:
        print(prefix_arr[x2][y2] - prefix_arr[x1-1][y2] - prefix_arr[x2][y1-1] + prefix_arr[x1-1][y1-1])