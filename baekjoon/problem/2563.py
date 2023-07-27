# 색종이
tot = 0
N = int(input())
my_list = []

for i in range(N):
    x1, y1 = map(int, input().split())
    for k in range(10):
        for m in range(10):
            temp = [x1+k, y1+m]
            if temp not in my_list:
                my_list.append(temp)   
    else:
        pass
# print(my_list)
print(len(my_list))
