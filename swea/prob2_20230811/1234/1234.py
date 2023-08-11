import sys
sys.stdin = open('input.txt')

# 비밀번호 / 202308011

T = 10

for tc in range(1, T+1):
    N, pa = map(str, input().split())
    N = int(N)
    stack = []
    for i in range(N):
        if stack and (stack[-1] == pa[i]):
            stack.pop()
        else:
            stack.append(pa[i])

    ans = ''.join(stack)
    print(f'#{tc} {ans}')

