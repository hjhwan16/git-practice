#첫 글자를 대문자로
N = int(input())
for i in range(N):
    word = str(input())
    word = word[0].upper() + word[1:]
    print(word)