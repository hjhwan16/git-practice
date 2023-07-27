# 수 정렬하기 3
# 수의 범위가 적다면 카운팅 정렬을 사용하여 더욱 빠르게 정렬할 수 있습니다.
# list.sort() 가 오래걸림


N = int(input())
num_list = []
for i in range(N):
    num = int(input())
    num_list.append(num)

cnt_list = [0] * (max(num_list) + 1)

for num in num_list:
    cnt_list[num] += 1

# print(cnt_list)

for k in range(len(cnt_list)):
    if cnt_list[k] == 0:
        pass
    else:
        for l in range(cnt_list[k]):
            print(k)