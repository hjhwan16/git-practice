a, b, c = map(int, input().split())
num_lst = [a, b, c]
num_lst.sort()
for i in num_lst:
    print(i, end=' ')