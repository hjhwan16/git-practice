col_arr = []
num_arr = []
for _ in range(5):
    temp = list(input().split())
    col_arr.append(temp[0])
    num_arr.append(int(temp[1]))
# print(col_arr)
# print(num_arr)
col_cnt_list = [0] * 4 # R, B, Y, G 순서
num_cnt_list = [0] * 10
for i in range(5):
    if col_arr[i] == 'R':
        col_cnt_list[0] += 1
    elif col_arr[i] == 'B':
        col_cnt_list[1] += 1
    elif col_arr[i] == 'Y':
        col_cnt_list[2] += 1
    else:
        col_cnt_list[3] += 1

for i in range(5):
    num_cnt_list[num_arr[i]] += 1

# print(num_cnt_list)

flag = False
for i in range(1, 6):
    if num_cnt_list[i:i+5] == [1,1,1,1,1]:
        flag = True

if max(col_cnt_list) == 5 and flag:
    ans = 900 + max(num_arr)
elif max(num_cnt_list) == 4:
    ans = 800 + num_cnt_list.index(4)
elif 3 in num_cnt_list and 2 in num_cnt_list:
    ans = 700 + 10 * num_cnt_list.index(3) + num_cnt_list.index(2)
elif max(col_cnt_list) == 5:
    ans = 600 + max(num_arr)
elif flag:
    ans = 500 + max(num_arr)
elif 3 in num_cnt_list:
    ans = 400 + num_cnt_list.index(3)
elif num_cnt_list.count(2) == 2:
    # print('2')
    temp = []
    for i in range(10):
        if num_cnt_list[i] == 2:
            temp.append(i)
            # print(temp)
    ans = 300 + 10*max(temp) + min(temp)
elif 2 in num_cnt_list:
    ans = 200 + num_cnt_list.index(2)
else:
    ans = 100 + max(num_arr)

print(ans)
