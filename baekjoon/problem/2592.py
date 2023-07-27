#평균과 최빈값 구하기
num_list = []
for i in range(10):
    num = int(input())
    num_list.append(num)

for k in range(len(num_list)):
    if k == 0:
        most_num = num_list[k]
    else:
        if num_list.count(num_list[k]) >= num_list.count(most_num):
            most_num = num_list[k]

print(int((sum(num_list)/len(num_list))))
print(most_num)
