tot = 0
tot_lst = []
for i in range(10):
    num_out, num_in = map(int, input().split())
    tot = tot + num_in - num_out
    tot_lst.append(tot)
print(max(tot_lst))