import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    arr = list(map(str, input().split()))
    stack = [0] * 256
    top = -1

    for i in arr:
        if i not in '+-*/.':
            top += 1
            stack[top] = int(i)
        
        # .이 나왔지만 stack에 1개 이상 남는 경우 예외처리
        elif i == '.':
            if top == 0:
                ans = stack[top]
                top -= 1
            else:
                ans = 'error'
                break
        # 연산자가 나왔지만 stack에 숫자가 2개 미만인 경우 예외처리
        else:
            if top < 1:
                ans = 'error'
                break
            else:
                s1 = stack[top]
                top -= 1
                s2 = stack[top]
                top -= 1

                if i == '+':
                    s3 = s2 + s1

                elif i == '-':
                    s3 = s2 - s1

                elif i == '*':
                    s3 = s2 * s1

                elif i == '/':
                    s3 = s2 // s1

                top += 1
                stack[top] = s3

    print(f'#{tc} {ans}')

