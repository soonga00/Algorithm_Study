import sys
input = sys.stdin.readline

E, S, M = map(int, input().split())

a, b, c = 1, 1, 1
year = 1
while True:
    if a == E and b == S and M == c:
        print(year)
        break
    a = a % 15 + 1
    b = b % 28 + 1
    c = c % 19 + 1
    year += 1
