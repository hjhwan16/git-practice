# 수 정렬하기 2
N = int(input())
num_list = []
for i in range(N):
    num = int(input())
    num_list.append(num)
num_list.sort()

for num in num_list:
    print(num)
