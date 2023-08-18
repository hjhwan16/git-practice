'''
15
push 1
push 2
front
back
size
empty
pop
pop
pop
size
empty
pop
push 3
empty
front

'''
import sys
input = sys.stdin.readline

N = int(input())
Q = [0] * N
front = -1
rear = -1
for _ in range(N):
    comp = list(map(str, input().split()))
    if comp[0] == 'push':
        rear += 1
        Q[rear] = int(comp[1])
    elif comp[0] == 'pop':
        if front == rear:
            print(-1)
        else:
            front += 1
            print(Q[front])
    elif comp[0] == 'size':
        print(rear - front)
    elif comp[0] == 'empty':
        if front == rear:
            print(1)
        else:
            print(0)
    elif comp[0] == 'front':
        if front == rear:
            print(-1)
        else:
            print(Q[front+1])
    elif comp[0] == 'back':
        if front == rear:
            print(-1)
        else:
            print(Q[rear])


