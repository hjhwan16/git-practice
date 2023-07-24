words = str(input())
words = words.lower()

word_list=list(set(words))

#print(word_list)
count_list=[]
for i in word_list:
    count_list.append(words.count(i))

#print(count_list)

if count_list.count(max(count_list))>1:
    print("?")
else:
    print(word_list[(count_list.index(max(count_list)))].upper())