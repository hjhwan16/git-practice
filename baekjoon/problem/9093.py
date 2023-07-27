
T = int(input())
for i in range(T):
    new_list = []
    word_list = list(map(str, input().split(' ')))

    for word in word_list:
        new_list.append(word[::-1])

    print(' '.join(new_list)) 