name_set = set()
n = int(input())
for i in range(n):
    name, status = map(str, input().split())
    if status == 'enter':
        name_set.add(name)
    else:
        name_set.remove(name)

# print(name_set)

# name_list = list(name_set)
# name_list.sort(reverse = True)

for i in sorted(name_set, reverse = True):
    print(i)

