# 기상캐스터 / 20230824
import sys
sys.stdin = open('input.txt')

# 현 상황 입력받기
# 구름이동 구현하기
# 각 구역에서 구름이 오는 시간 구현하기(W분 동안만 구현하면 됨)

H, W = map(int, input().split())
arr = []
for _ in range(H):
    temp = list(input())
    arr.append(temp)

# 구름지도 -1이 구름만난적 없음을 나타냄
cloud_arr = [[-1]*W for _ in range(H)]

# 확인해야 하는 분 기준 확인 -> 이동
for min in range(W):
    # 구름 체크
    for i in range(H):
        for j in range(W):
            # 현재 구름이 있고 구름을 만난적이 없다면
            if arr[i][j] == 'c' and cloud_arr[i][j] == -1:
                cloud_arr[i][j] = min
    # 구름 이동
    for i in range(H):
        arr[i].pop()
        arr[i] = ['.'] + arr[i]
for i in range(H):
    for j in range(W):
        print(cloud_arr[i][j], end=' ')
    print()
