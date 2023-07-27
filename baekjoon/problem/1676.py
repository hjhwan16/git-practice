# 팩토리얼 0의 개수
tot = 1
cnt = 0
N = int(input())
for i in range(1, N+1):
    tot *= i
# print(tot) 

tot_list = list(str(tot))[::-1]

# print(tot_list)

for k in tot_list:
    if k == '0':
        cnt += 1
    else:
        print(cnt)
        break 