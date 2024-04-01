def print_stack(s):
    if len(s) == 0:
        return
    while len(s) > 0:
        print(s.pop(), end="")

stack = []
arr = input()
flag = False
for i in arr:
    if i == '<':
        print_stack(stack)
        flag = True
        print(i, end="")
    elif i == '>':
        print(i, end="")
        flag = False
    elif flag:
        print(i, end="")
    elif i == ' ':
        print_stack(stack)
        print(" ", end="")
    else:
        stack.append(i)
print_stack(stack)
