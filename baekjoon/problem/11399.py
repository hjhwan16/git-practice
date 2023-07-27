# ATM
each_min = 0
tot_min = 0

N = int(input())
mininutes = list(map(int, input().split()))

mininutes.sort()

for min in mininutes:
    each_min += min
    tot_min += each_min

print(tot_min)