pib_list = []
n = int(input())
for i in range(n+1):
    if i == 0:
        pib_list.append(0)
    elif i == 1:
        pib_list.append(1)
    else:
        pib_list.append(pib_list[i-2] + pib_list[i-1])

print(pib_list[n])