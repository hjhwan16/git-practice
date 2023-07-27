tot = 0
my_lst = []
for i in range(4):
    out_num, in_num = map(int, input().split())
    tot = tot - out_num + in_num
    my_lst.append(tot)
print(max(my_lst)) 