def print_num(queue, i):
    num = 0
    j = 0
    while len(queue) > 0:
        p = max(queue)
        if queue[j] < p:
            if i == j:
                i = len(queue) - 1
            else:
                i -= 1
            queue.append(queue.pop(0))
        else:
            num += 1
            if i == j:
                print(num)
                break
            else:
                queue.pop(0)
                i -= 1


T = int(input())

for _ in range(T):
    N, M = map(int, input().split())
    queue = list(map(int, input().split()))
    print_num(queue, M)