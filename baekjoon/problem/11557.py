Testcase = int(input())

for k in range(Testcase):
    number = int(input())
    name_lst = []
    number_lst = []
    for i in range(number):
        name, number2 = input().split()
        name_lst.append(name)
        number_lst.append(int(number2))
    print(name_lst[number_lst.index(max(number_lst))])
