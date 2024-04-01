import sys
input = sys.stdin.readline
t = int(input())

for _ in range(t):
    n = int(input())

    employee = [list(map(int, input().split())) for i in range(n)]
    employee.sort()

    top = 0
    result = 1

    for i in range(1,n):
        if employee[i][1] < employee[top][1]:
            top = i
            result += 1
    print(result)