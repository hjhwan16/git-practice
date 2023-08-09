import sys
sys.stdin = open('input.txt')

# 괄호검사 / 스택 / 20230809

# 괄호가 제데로 이어진 경우 1을 아닌 경우 0을 출력

# 괄호의 종류 ({})

T = int(input())
for tc in range(1, T+1):
    word = input()
    answer = 1

    stack = [0] * len(word)
    top = -1

    for i in range(len(word)):
        # ( 혹은 { 인 경우 stack에 담기
        if word[i] == '(' or word[i] == '{':
            top += 1
            stack[top] = word[i]
        # ) 혹은 } 인경우 stack 최상단과 비교 후 제거 혹은 stop
        elif word[i] == ')':
            # stack 최 상단이 ( 인 경우 0으로 바꿔주고 top -1
            if stack[top] == '(':
                stack[top] = 0
                top -= 1
            else:
                answer = 0
                break
        elif word[i] == '}':
            # stack 최 상단이 { 인 경우 0으로 바꿔주고 top -1
            if stack[top] == '{':
                stack[top] = 0
                top -=1
            else:
                answer = 0
                break
        else:
            pass

    # stack 에 괄호가 남아있는 경우
    if top != -1:
        answer = 0

    print(f'#{tc} {answer}')

