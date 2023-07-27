case = int(input())
for i in range(case):
    num = int(input())
    tot_c = 0
    tot_g = 0
    total = 0
    for k in range(num):
        c, g = input().split()
        tot_c += int(c)
        tot_g += float(g)
        total += float(c) * float(g)
    print(tot_c, round((total/tot_c),1))
