while True:
    password = str(input())
    if password == 'END':
        break
    else:
        pass_lst = list(password)
        pass_lst = pass_lst[::-1]
        for s in pass_lst:
            print(s, end ='')
        print()