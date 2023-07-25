# 듣보잡

N, M = map(int, input().split())

set1 = set()
set2 = set()

for i in range(N):
    name1 = str(input())
    set1.add(name1)

for k in range(M):
    name2 = str(input())
    set2.add(name2)

set3 = set1 & set2

set3 = sorted(set3)

print(len(set3))
for name in set3:
    print(name)

