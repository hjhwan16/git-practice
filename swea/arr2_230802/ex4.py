# 대각선으로 접근
N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
total1 = 0
# 좌상 우하
for i in range(N):
    total1 += arr[i][i]
# 우상 좌하
total2 = 0
for k in range(N):
    total2 += arr[i][N-1-i]