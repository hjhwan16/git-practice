current_time = list(map(int, input().split(':')))
start_time = list(map(int, input().split(':')))

if current_time[2] > start_time[2]:
    second = start_time[2] + 60 - current_time[2]
    current_time[1] += 1

elif current_time[2] <= start_time[2]:
    second = start_time[2] - current_time[2]

if current_time[1] > start_time[1]:
    minute = start_time[1] + 60 - current_time[1]
    current_time[0] += 1

elif current_time[1] <= start_time[1]:
    minute = start_time[1] - current_time[1]

if current_time[0] > start_time[0]:
    hour = start_time[0] + 24 - current_time[0]
    current_time[0] += 1

elif current_time[0] <= start_time[0]:
    hour = start_time[0] - current_time[0]

print(f'%02d:' %hour, end='')
print(f'%02d:' %minute, end='')
print(f'%02d' %second)