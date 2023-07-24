# 광고
L = int(input())
word = str(input())
check_list = []

for i in range(1, L+1):
    check_word = word * i
    print(check_word)
    for k in range(L):
        temp = check_word[k*i: k*i+i]
        print(k, temp)
        check_list.append(temp)
    print(check_list)
    if len(set(check_list)) == 1:
        print(i)
        break
    else:
        check_list = []
