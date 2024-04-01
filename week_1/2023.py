import math

def is_prime(a):
    if a == 1:
        return False
    for i in range(2, int(math.sqrt(a)) + 1):
        if a % i == 0:
            return False
    return True

def find_prime(num, n):
    if len(str(num)) == n:
        print(num)
    if is_prime(num):
        for i in range(1, 10):
            if is_prime(num*10 + i):
                find_prime(num*10 + i, n)

n = int(input())
find_prime(2, n)
find_prime(3, n)
find_prime(5, n)
find_prime(7, n)