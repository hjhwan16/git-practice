import sys
sys.stdin = open('input.txt')

T = 10
for tc in range(1, 11):
    n = int(input())    # 문자열계산식의 길이
    fx = str(input())    # 문자열 입력받기
    s = ''
    ans = 0
    stack = []
    # 후위 연산자로 바꿔주기
    for x in fx:
        if x != '+':
            s += x
        else: # x == '+'
            if not stack: # 스택이 비었다면
                stack.append(x)
            else:
                while stack:
                    s += stack.pop()
                stack.append(x)
    if stack:
        s += stack.pop()
    print(s)
    # 후위 연산자 계산해주기
    stack = []
    for x in s:
        if x != '+':
            stack.append(int(x))
        else:
            s1 = stack.pop()
            s2 = stack.pop()
            s3 = s2 + s1
            stack.append(s3)
    ans = stack[-1]

    print(f'#{tc} {ans}')