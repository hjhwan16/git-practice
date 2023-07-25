N = int(input())
name_list = []
for i in range(N):
    age, name = map(str, input().split())
    name_list.append([int(age), name])

name_list.sort(key = lambda x: x[0])

for k in name_list:
    for m in k:
        print(m, end = ' ')
    print()