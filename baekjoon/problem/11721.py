word = str(input())
cnt = 0
for i in range(len(word)):
    print(word[i], end='')
    cnt += 1
    if cnt == 10:
        cnt = 0
        print()