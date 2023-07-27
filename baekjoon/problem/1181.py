word_list = []

N = int(input())

for i in range(N):
    word = str(input())
    if word in word_list:
        pass
    else:
        word_list.append(word)

word_list.sort(key = lambda x: (len(x), x))

for k in word_list:
    print(k)