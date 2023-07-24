# 대표값2
num_list = []
for i in range(5):
    num = int(input())
    num_list.append(num)

num_list.sort()
print(int(sum(num_list)/len(num_list)))
print(num_list[2])
