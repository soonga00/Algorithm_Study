import sys
def cal_idx(time):
    h, m, s = map(int, time.split(':'))
    return (((h*60)+m)*60)+s

def add_arr(s_idx, e_idx):
    t_arr[s_idx] += 1
    t_arr[e_idx] += 1

def cal_prefix_sum():
    v = t_arr[0]
    prefix_sum[0] = v
    for i in range(1, 86398):
        v += t_arr[i]
        prefix_sum[i] = prefix_sum[i-1] + v

def find_max(len):
    max = prefix_sum[len-1]
    cal_prefix_sum()
    for i in range(0, max_idx-len+1):
        sum = prefix_sum[len+i-1] - prefix_sum[i-1]
        if sum > max:
            max = sum
            print(f'max = {max}, {i} ~ {len+i}')
    return max

t_arr = [0] * 86400
prefix_sum = [0] * 86400
min_idx = 86399
max_idx = 0
num = int(sys.stdin.readline())

for i in range(num):
    cmd = sys.stdin.readline()
    if int(cmd[0]) == 1:
        a, b, c = cmd.split()
        start_idx = cal_idx(b)
        end_idx = cal_idx(c)
        if start_idx < min_idx:
            min_idx = start_idx
        if end_idx > max_idx:
            max_idx = end_idx
        add_arr(start_idx, end_idx)
    else:
        a, b = cmd.split()
        c = cal_idx(b)
        print(find_max(c))
