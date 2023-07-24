#백설 공주와 일곱 난쟁이
from itertools import combinations
num_list = []
for i in range(9):
    num = int(input())
    num_list.append(num)
total = sum(num_list) 
#print(total)

comb_list = list(combinations(num_list, 2))

for k in comb_list:
    if sum(k) == (total - 100):
        del_list = list(k)
num_list.sort()
for m in num_list:
    if m not in del_list:
        print(m)