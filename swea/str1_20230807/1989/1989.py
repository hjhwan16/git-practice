import sys
sys.stdin = open('input.txt')

T = int(input())

# for tc in range(1, T+1):
#     word = str(input())
#     ans = 0
#     if word == word[::-1]:
#         ans = 1
#     print(f'#{tc} {ans}')

for tc in range(1, T+1):
    word = str(input())
    ans = 0
    N = len(word)
    for i in range(N//2):
        if word[i] == word[N-i-1]:
            ans = 1
        else:
            ans = 0
    print(f'#{tc} {ans}')

