# 좌표 정렬하기
N = int(input())
my_list = []

for i in range(N):
    x, y = map(int, input().split())
    my_list.append([x, y])

my_list.sort(key = lambda x: (x[1], x[0]))

# print(my_list)

for k in my_list:
    for j in k:
        print(j, end=' ')
    print()
             
