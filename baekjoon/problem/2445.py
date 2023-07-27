num = int(input())
for i in range(1, num+1):
    print('*' * i, end = '')
    print(' ' * (2*(num - i)), end='')
    print('*' * i)
for k in range(1, num):
    print('*' * (num - k), end='')
    print(' ' * (2*k), end='')
    print('*' * (num - k))