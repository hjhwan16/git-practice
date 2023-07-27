num = int(input())
cnt = 1
for i in range(num):
    if cnt % 2 == 1:
        print('* ' * num)
        cnt = cnt + 1
    else:
        print(' *' * num)
        cnt = cnt + 1
