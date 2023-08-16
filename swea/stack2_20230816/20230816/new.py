import sys
sys.stdin = open('input.txt')

T = 10

for tc in range(1, T + 1):
    N = int(input())
    arr = str(input())

    # 후위 표기법으로 변환
    stack = [0] * N
    top = -1
    icp = {'*': 2, '+': 1}
    isp = {'*': 2, '+': 1}

    equation = ''
    for x in arr:
        if x not in '+*':  # 피연산자
            equation += x
        else:  # '+*'
            if top == -1 or isp[stack[top]] < icp[x]:  # 들어오는 priority가 높은 경우
                top += 1  # push
                stack[top] = x
            elif isp[stack[top]] >= icp[x]:
                while top > -1 and isp[stack[top]] >= icp[x]:
                    equation += stack[top]
                    top -= 1
                top += 1
                stack[top] = x
    while top > -1:
        equation += stack[top]
        top -= 1



    # 후위 표기법 에서 연산
    stack_2 = [0] * N
    top = -1
    for x in equation:
        if x not in '+-*/':  # 피연산자이면
            top += 1  # push(x)
            stack_2[top] = int(x)
        else:
            op1 = stack_2[top]  # pop()
            top -= 1
            op2 = stack_2[top]  # pop()
            top -= 1
            if x == '+':  # op2 + op1
                top += 1  # push
                stack_2[top] = op2 + op1
            elif x == '*':  # op2 * op1
                top += 1  # push
                stack_2[top] = op2 * op1

    print(f'#{tc} {stack_2[top]}')
