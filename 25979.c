#include <stdio.h>
#include <string.h>

double in_arr[86400];
double prefix_sum[86400];

int cal_idx(int h, int m, int s)
{
    return (3600*h + 60*m + s);
}

void add_arr(int s_idx, int e_idx)
{
    in_arr[s_idx]+=1;
    if (e_idx < 86400)
        in_arr[e_idx]-=1;
}

void cal_prefix_sum()
{
    double v = in_arr[0];
    prefix_sum[0] = in_arr[0];
    for(int i = 1; i < 86400; i++){
        v += in_arr[i];
        prefix_sum[i] = prefix_sum[i-1] + v;
    }
}

double find_max(int len)
{
    double max = prefix_sum[len-1];
    double sum;
    cal_prefix_sum();
    for (int i = 1; i < 86400-len+1; i++)
    {
        sum = prefix_sum[len+i-1] - prefix_sum[i-1];
        if (sum > max){
            max = sum;
        }
    }
    return max;
}

int main(void)
{
    int num, start_idx, end_idx, cmd;
    scanf("%d", &num);
    memset(in_arr, 0, sizeof(double)*86400);
    for (int i = 1; i < num; i++)
    {
        scanf("%d", &cmd);
        if (cmd == 1)
        {
            int h1, h2, m1, m2, s1, s2;
            scanf("%d:%d:%d %d:%d:%d", &h1, &m1, &s1, &h2, &m2, &s2);
            start_idx = cal_idx(h1, m1, s1);
            end_idx = cal_idx(h2, m2, s2);
            add_arr(start_idx, end_idx);
        }
    }
    scanf("%d", &cmd);
    if (cmd == 2)
    {
        int h3, m3, s3, t;
        scanf("%d:%d:%d", &h3, &m3, &s3);
        t = cal_idx(h3, m3, s3);
        printf("%.0lf\n", find_max(t));
    }
    return 0;
}
