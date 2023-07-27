number = int(input())
lst = []

if number == 1:
    lst =[1]

for i in range(1, number):
    if number - i >= 0:
        lst.append(i)
        number -= i
    else:
        break

print(len(lst))
