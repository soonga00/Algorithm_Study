N = int(input())
meetings=[]
for i in range(N):
    meetings.append(list(map(int,input().split())))
meetings=sorted(meetings,key=lambda x:x[1])
print(meetings)
max_meetings = 0
end_time = 0
for i in meetings:
    if i[0] >= end_time:
        max_meetings += 1
        end_time = i[1]
print(max_meetings)