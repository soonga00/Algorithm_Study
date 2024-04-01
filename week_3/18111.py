N, M, B = map(int, input().split())
ground = []
min_t = 2147483647
max_height = 0
for _ in range(N):
    ground.append(list(map(int, input().split())))

for i in range(257):
    get_block = 0
    use_block = 0
    for j in range(N):
        for k in range(M):
            if ground[j][k] >= i:
                block = ground[j][k] - i
                get_block += block
            else:
                block = i - ground[j][k]
                use_block += block
    if use_block - get_block <= B:
        t = get_block*2 + use_block
        if t < min_t:
            min_t = t
            max_height = i
        elif t == min_t and max_height < i:
            max_height = i
print(min_t, max_height)