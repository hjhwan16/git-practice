# 오름차순 정렬
N = int(input())
num_list = []

for i in range(N):
    num = int(input())
    num_list.append(num)

num_list.sort()

for k in num_list:
    print(k)