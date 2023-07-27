n = int(input())
num_lst = []
for i in range(0, n + 1):
    if i == 0:
        num_lst.append(0)
    elif i == 1:
        num_lst.append(1)
    else:
        num_lst.append(num_lst[i - 1] + num_lst[i - 2])
print(num_lst[n])
