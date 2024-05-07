import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    a, b = map(int, input().split())
    while True:
        if a > b:
            if a % 2 == 1:
                a-=1
            a//=2
        elif a < b:
            if b % 2 == 1:
                b-=1
            b//=2
        else:
            print(a*10)
            break