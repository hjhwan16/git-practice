# 제로
num_list = []
K = int(input())
for i in range(K):
    num = int(input())
    if num == 0:
        num_list.pop()
    else:
        num_list.append(num)
print(sum(num_list))