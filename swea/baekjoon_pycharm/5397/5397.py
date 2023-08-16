# 키로거 / 20230816

T = int(input())

for tc in range(1, T+1):
    fx = str(input)
    L = len(fx)

    stack = [0] * L
    top = -1
    cnt = 0 #출력해야 하는 글자의 갯수

    for x in fx:
        if x == '>':

        elif x == '<':

        elif x == '-':
            cnt -= 1

        else:
            cnt += 1