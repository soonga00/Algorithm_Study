N = int(input())
M = int(input())
S = input()
num = 0
P = 0
i = 0

while i < (M - 1):
    if S[i:i+3] == 'IOI':
        i += 2
        P += 1
        if P == N:
            num += 1
            P -= 1
    else:
        i += 1
        P = 0
        
print(num)