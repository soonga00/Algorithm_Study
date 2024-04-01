num = input()
arr = list(num)
num = int(num)

if not '0' in arr or len(arr) < 2:
    print(-1)
else:
    if num % 3 != 0:
        print(-1)
    else:
        arr.sort(reverse=True)
        print("".join(arr))