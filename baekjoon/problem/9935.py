# 문자열 폭발

sen = str(input())
bomb = str(input())

stack = []

# 하나씩 넣으면서 확인
for i in range(len(sen)):
    # stack의 길이가 bomb의 길이보다 크거나 같다면
    if len(stack) + 1 >= len(bomb):
        # 같은지 확인
        # bomb가 되는 지 확인
        check = ''
        for j in range((len(bomb)-1)):
            check += stack[-len(bomb)+1+j]
        if check + sen[i] == bomb:
            for k in range(len(bomb)-1):
                stack.pop()
        else:
            stack.append(sen[i])
    else:
        stack.append(sen[i])

if len(stack) == 0:
    print('FRULA')
else:
    for i in stack:
        print(i, end='')