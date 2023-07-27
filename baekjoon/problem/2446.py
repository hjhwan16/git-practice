num = int(input())

for i in range(num):
    print(' ' * i, end = '')
    print('*' * ((2 * (num - i))-1))
for k in range(1, num):
    print(' ' * ((num - k) - 1), end='')
    print('*' * (2 * k + 1))