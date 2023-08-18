import sys
sys.stdin = open('input.txt')

T = 10
for tc in range(1, T+1):
    tc = int(input())
    Q = list(map(int, input().split()))
    front = 0
    rear = 7
    cnt = 0

    while True:
        # 1,2,3,4,5 순서대로 빼주고
        Q[front] -= (cnt % 5) + 1
        cnt += 1
        # 0보다 작거나 같아지면 0으로 바꿔주고 break
        if Q[front] <= 0:
            Q[front] = 0
            break
        # front 하나씩 증가 (원형큐)
        front = (front + 1) % 8

    # print(Q, front)

    print(f'#{tc}', end=' ')
    for i in range(front + 1, 8):
        print(Q[i], end= ' ')
    for i in range(front+1):
        print(Q[i], end=' ')
    print()