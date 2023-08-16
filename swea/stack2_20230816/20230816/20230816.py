import sys
sys.stdin = open('input.txt')


T = 10

for tc in range(1, T+1):
    N = int(input())
    fx = str(input())

    stack = [0] * N
    top = -1
    s = ''
    icp = {'*': 2, '+': 1}
    isp = {'*': 2, '+': 1}

    # 후위 계산식 만들기
    for x in fx:
        if x not in '*+': #수식인 경우 그냥 더하기
            s += x
        else: # 수식인 경우 조건에 맞게 stack에 추가
            if top == -1 or isp[stack[top]] < icp[x]:
                top += 1
                stack[top] = x
            elif isp[stack[top]] >= icp[x]:
                while top > -1 and isp[stack[top]] >= icp[x]:
                    s += stack[top]               # 조건에 맞게 s에 추가 해주기
                    top -= 1
                top += 1
                stack[top] = x

    # 나머지 다 뽑아내기
    while top > -1:
        s += stack[top]
        top -= 1

    # print(stack)

    #계산하기
    stack = [0] * N
    top = -1
    num = 0
    formular = 0
    for x in s:
        if x not in '*+':
            top += 1
            stack[top] = int(x)
        else:
            s1 = stack[top]
            top -= 1
            s2 = stack[top]
            top -= 1
            if x == '*':
                top += 1
                stack[top] = s1 * s2
            elif x == '+':
                top += 1
                stack[top] = s1 + s2

    # print(stack)
    ans = stack[top]

    print(f'#{tc} {ans}')



