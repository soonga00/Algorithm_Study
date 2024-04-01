import sys
import math
input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))
arr.sort()
a = (n+1)//2
num = 0
for i in range(a):
    num += int(math.log2(arr[i]))
print(num+1)