import sys
input = sys.stdin.readline

n, k = map(int, input().split())
num = input().strip()
result = []

for i in num:
    while result and k > 0:
        if result[-1] < i:
            result.pop()
            k -= 1
        else: break
    result.append(i)
if k > 0:
    print("".join(result[:-k]))
else:
    print("".join(result))