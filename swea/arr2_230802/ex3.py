'''
3
1 2 3
4 5 6
7 8 9
'''
# delta 다른 방법
# 입력받기
N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
# 십자가 형태로 합을 구하고 최대값 구하기
m = 4
max_v = 0 # 모든 원소가 0이상이라면...
for i in range(N): # 모든 원소 arr[i][j]에 대해...
    for j in range(N):
        s = arr[i][j] # 일단 센터값으로 초기화
        for di, dj in [[0, 1], [1, 0], [0, -1], [-1, 0]]: # 상하좌우 이동 이런 방법 도 있다!
            # 해당 방향으로 한칸이 아닌 m칸을 가야한다면?
            for p in range(1, m):
                ni = i + di * p
                nj = j + dj * p
            # 배열 내부에 있으면
                if 0 <= ni < N and 0 <= nj < N:
                    s += arr[ni][nj]
        # 주변원소의 합을 구했음
        if max_v < s:
            max_v = s


