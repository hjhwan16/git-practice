import sys
from itertools import combinations
input = sys.stdin.readline

N = int(input())
my_dict = {}
for i in range(N):
    num = int(input())
    my_dict[i+1] = num
# print(my_dict)
up = list(my_dict.keys())
# print(up)
combi = []
for i in range(1, N):
    # print(list(combinations(up, i)))
    combi += (list(combinations(up, i)))
max_v = 0
max_set ={}
# print(combi)
for i in range(len(combi)):
    # print(combi[i])
    up_set = set(combi[i])
    down_set = set()
    for j in combi[i]:
        # print(my_dict[j], end= '')
        down_set.add(my_dict[j])
    # print()
    # print(up_set, down_set)
    if up_set == down_set:
        if max_v < len(up_set):
            max_v = len(up_set)
            max_set = up_set

    # combi[i] = list(combi[i])
print(max_v)
for i in max_set:
    print(i)