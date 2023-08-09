while True:
    word = str(input())
    answer = 'yes'

    if word == '.':
        break
    stack = [0] * len(word)
    top = -1

    for i in range(len(word)):
        # ( 혹은 { 인 경우 stack에 담기
        if word[i] == '(' or word[i] == '[':
            top += 1
            stack[top] = word[i]
        # ) 혹은 } 인경우 stack 최상단과 비교 후 제거 혹은 stop
        elif word[i] == ')':
            # stack 최 상단이 ( 인 경우 0으로 바꿔주고 top -1
            if stack[top] == '(':
                stack[top] = 0
                top -= 1
            else:
                answer = 'no'
                break
        elif word[i] == ']':
            # stack 최 상단이 { 인 경우 0으로 바꿔주고 top -1
            if stack[top] == '[':
                stack[top] = 0
                top -=1
            else:
                answer = 'no'
                break
        else:
            pass
    
    if top != -1:
        answer = 'no'
    
    print(answer)