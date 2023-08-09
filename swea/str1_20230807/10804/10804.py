import sys
sys.stdin = open('input.txt')

# 문자열을 거울에 비추면 나타나는?

my_dict = {'q':'p', 'p':'q', 'b':'d', 'd':'b'}

T = int(input())

for tc in range(1, T+1):
    word = input()
    word = word[::-1]
    ans = ''
    for i in word:
        ans += my_dict[i]
    print(f'#{tc} {ans}')
