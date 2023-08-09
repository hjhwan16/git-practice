# 스택2 / 20230809
import sys
# 정수를 저장하는 스택을 구현한 다음, 입력으로 주어지는 명령을 처리하는 프로그램을 작성하시오.
# 명령은 총 5가지

N = int(sys.stdin.readline())
stack = []

for c in range(N):
    cmd = sys.stdin.readline().split()

    # 명렬 1 x: 정수 x를 스택에 넣는다
    if cmd[0] == '1':
        stack.append(cmd[1])
    # 명렬 2: 스택에 정수가 있다면 맨 위의 정수를 출력 없으면 -1 출력
    elif cmd[0] == '2':
        if stack:
            print(stack.pop())
        else:
            print(-1)
    # 명렬3: 스택에 들어있는 정수의 개수를 출력
    elif cmd[0] == '3':
        print(len(stack))
    # 명렬4: 스택이 비어있으면 1 아니면 0
    elif cmd[0] == '4':
        if stack:
            print(0)
        else:
            print(1)
    # 명렬5: 맨 위의 정수를 출력 없으면 -1
    elif cmd[0] == '5':
        if stack:
            print(stack[-1])
        else:
            print(-1)