
stack = [0]*100
top = -1
# 우선순위 클수록 먼저
# 우선순위가 높으면 push
# 우선순의가 작으면 작아질때 까지 pop 후 push
# top = -1 이면 push

icp = {'(': 3, '*':2, '/':2, '+':1, '-':1}
isp = {'(': 0, '*':2, '/':2, '+':1, '-':1}



fx = input()
s = ''
for x in fx:
    if x not in '(+-*/)':
        s += x
    elif x == ')':
        # (가 나올때 까지 pop 후  ( 버림
        while stack[top] != '(':
            s += stack[top]
            stack[top] = 0
            top -= 1
        stack[top] = 0
        top -= 1

    # 수식이 나오는 경우
    else:
        if top == -1 or isp[stack[top]] < icp[x]:
            top += 1
            stack[top] = x
        elif isp[stack[top]] >= icp[x]:
            while top > -1 and isp[stack[top]] >= icp[x]:
                s += stack[top]
                stack[top] = 0
                top -= 1
            top += 1
            stack[top] = x
while top > -1:
        s += stack[top]
        stack[top] = 0
        top -= 1
print(s, stack)