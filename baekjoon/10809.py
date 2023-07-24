alphabet_list = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
word = list(input())
my_lst = []
for alphbet in alphabet_list:
    my_lst.append(word.count(alphbet))

for k in my_lst:
    print(k, end=' ')