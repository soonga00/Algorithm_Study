def gcd(m,n):
    if m < n:
        m, n = n, m
    if n == 0:
        return m
    if m % n == 0:
        return n
    else:
        return gcd(n, m%n)
        
def lcm(m, n):
	return (m * n) // gcd(m, n)

a, b = map(int, input().split())
c, d = map(int, input().split())

denom = lcm(b, d)
a = a * (denom // b)
c = c * (denom // d)
numer = a+c

gcd_num = gcd(numer, denom)
while (gcd_num != 1):
     numer //= gcd_num
     denom //= gcd_num
     gcd_num = gcd(numer, denom)
print(numer, denom)