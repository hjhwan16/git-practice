'''


'''
# N장의 카드가 있고 1번카드가 제일 위 N번 카드가 제일 아래인 상태
# 위[1, 2, 3, 4, 5, 6] 아래
# 제일 위에 있는 카드를 바닥에 버리고, 제일 위에 있는 카드를 제일 아래에 있는 카드 밑으로
# 마지막 남는 카드?

N = int(input())
Q = [i for i in range(1, N+1)]
front = -1
rear = N

# 1개의 카드가 남아야 하기 때문에 N-1번반복
for _ in range(N-1):
    # 제일 위에 있는 카드 버리기
    front += 1
    print(Q[front], end= ' ')
    # 제일 위에 있는 카드 제일 밑으로
    front += 1
    Q.append(Q[front])
print(Q[-1])
