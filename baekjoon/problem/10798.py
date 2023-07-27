# 세로 읽기

my_list = []
len_list = []

for i in range(5):
    temp = list(str(input()))
    my_list.append(temp)

# for j in my_list:
#     len_list.append(len(my_list))

for k in range(15):
    for m in range(5):
        if k < len(my_list[m]):
            print(my_list[m][k], end='')