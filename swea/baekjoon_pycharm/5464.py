'''
3 4
2
3
5
200
100
300
800
3
2
-3
1
4
-4
-2
-1

'''

N, M = map(int, input().split())
# idx 0 -> 1번 /// idx N-1 -> N번


ans = 0
parking = [0] * (N+1)
S = [0] * (N+1)      # 주차장 가격 list S
W = [0] * (M+1)      # 대기열 차량의 무게
move = [0] * (2*M + 1)
visited = [0] * (N+1)
for i in range(1, N+1):
    S[i] = int(input())     # [0, 2, 3, 5]
for i in range(1, M+1):
    W[i] = int(input())     # [0, 200, 100, 300, 800]
for i in range(1, 2*M+1):
    move[i] = int(input())  # [3, 2, -3, 1, 4, -4, -2, -1]


queue = []
# 들어오때 계산
for i in range(2*M):
    mov = move.pop(0)
    if mov > 0:     # 들어오는 경우
        queue.append(mov)
    else:
        mov *= -1
        idx = parking.index(mov)
        visited[idx] = 0
    for k in range(1, N+1):
        if visited[k] == 0 and queue: # k번째로 투입
            visited[k] = 1
            car_in = queue.pop(0)
            ans += W[car_in] * S[k]
            parking[k] = car_in
            break

print(ans)