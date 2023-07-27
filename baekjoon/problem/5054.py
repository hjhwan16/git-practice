# 주차의 신
t = int(input())
for i in range(t):
    n = int(input())
    location_list = list(map(int, input().split()))
    print(2 * (max(location_list) - min(location_list)))