
import copy# 더하기 사이클
num = int(input())
origin_num = copy.deepcopy(num)
# 주어진 수가 10보다 작다면
# if num < 10:
#     num = int(str(0) + str(num))

# # 새로운 수는 
# sum_num = num // 10 + num % 10
# # str(num[0]) + str(num[1])

# num = int(str(num)[1] + str(sum_num)[-1])

cnt = 0
while True:
    if num < 10:
        num = str(0) + str(num)
    sum_num = int(str(num)[0])  + int(str(num)[1])
    num = int(str(num)[1] + str(sum_num)[-1])
    cnt += 1
    if num == origin_num:
        print(cnt)
        break 



