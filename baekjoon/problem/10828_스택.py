# 10828 스택 # 시간초과
# 스택의 개념을 익히고 실습하는 문제

# push X: 정수 x를 스택에 넣는 연산
# def push(x):
import sys

N = int(input())
stack = []

for i in range(N):
    method = sys.stdin.readline().rstrip()
    if method[:4] == 'push':
        method, num = method.split(' ')
        stack.append(num)
        # print(stack)
    else:
        if method == 'pop':
            # 스택 가장 위에 있는 정수를 뻬고 그 수를 출력
            # 없는 경우 -1 출력
            if not stack:
                print(-1)
            else:
                print(stack.pop()) 

        elif method == 'size':
            # 스택에 들어있는 정수의 개수를 출력
            print(len(stack))
            
        # elif method == 'push':
        #     # 정수X를 스택에 넣는 연산
            
            
        elif method == 'empty':
            # 스택이 비었다면 1 아니면 0을 출력
            if not stack:
                print(1)
            else:
                print(0)

        elif method == 'top':
            # 스택에 가장 위에 있는 정수
            if not stack:
                print(-1)
            else:
                print(stack[-1])
            