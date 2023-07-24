lst = []
for i in range(7):
    a = int(input())
    if a % 2 == 1:
        lst.append(a)
lst.sort()
if lst == []:
    print(-1)
else:
    print(sum(lst))
    print(min(lst))