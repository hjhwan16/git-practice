# 가장 큰 금민수
# 완전 탐색

N = int(input())
set_list = []

for i in range(N + 1):
    temp_set = set(list(str(i)))
    # print(temp_set)
    if temp_set.issubset({'4', '7'}):
        set_list.append(i)
        # print('당첨')

print(set_list[-1])