import sys
input = sys.stdin.readline
def mod(a, b, c):
    if b == 1:
        return a%c
    result = mod(a, b//2, c)
    if b%2 == 0:
        return (result * result) % c
    else:
        return (result * result * a) % c
    
a, b, c = map(int, input().split())

print(mod(a, b, c))  