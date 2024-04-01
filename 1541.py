import sys
input = sys.stdin.readline
str = input().split('-')
min_num = sum(map(int, str[0].split('+')))
if len(str) != 1:
    for i in str[1:]:
        n = sum(map(int, i.split('+')))
        min_num -= n 
print(min_num)