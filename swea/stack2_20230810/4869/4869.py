import sys
sys.stdin = open('input.txt')


def factorial(x):
    if x > 1:
        return x * factorial(x-1)
    else:
        return 1


T = int(input())

for tc in range(1, T+1):
    N = int(int(input()) / 10)
    ans = 1
    # N-i Combi i 를 만들어 주고 각 경우에 대해서 (2**i - 1) 를 곱해줌
    # + N - i Combi i 이기 때문에 N-i Combi i 이기 떄문에 소거 됨
    for i in range(1, (N // 2) + 1):
        ans += int(factorial(N-i) / (factorial(i)*factorial(N - 2*i))) * (2**i)

    print(f'#{tc} {ans}')