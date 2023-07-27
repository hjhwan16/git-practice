number = int(input())
cnt = 0
while True:
    if number == 0:
        break
    else:
        print(' '*cnt, end='')
        print('*'*number)
        cnt+=1
        number -= 1