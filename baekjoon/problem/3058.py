# 짝수를 찾아라
T = int(input())
for i in range(T):
    num_list = list(map(int, input().split()))
    even_num_list = []
    for num in num_list:
        if num % 2 == 0:
            even_num_list.append(num)
    print(sum(even_num_list), min(even_num_list))

