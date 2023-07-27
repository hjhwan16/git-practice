min_num = int(input())
max_num = int(input())
num_lst = []
for num in range(min_num, max_num + 1):
    if (num**(1/2)) % 1 == 0:
        num_lst.append(num)

if len(num_lst) == 0:
    print(-1) 
else:
    print(sum(num_lst))
    print(min(num_lst))