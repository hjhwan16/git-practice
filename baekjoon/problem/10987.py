#모음의 개수
alpha = ['a', 'e', 'i', 'o', 'u']
word = str(input())
cnt = 0

for i in word:
    if i in alpha:
        cnt += 1

print(cnt) 
