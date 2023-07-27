# N번째 큰 수
T = int(input())
for i in range(T):
    num_list = list(map(int, input().split()))
    num_list.sort()
    print(num_list[-3])