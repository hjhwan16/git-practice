num = int(input())
for i in range(num+1):
    print(' '*(i), end='')
    print('*'*(2*num - (2*i+1)))
