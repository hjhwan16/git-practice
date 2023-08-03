# delta
'''
3
1 2 3
4 5 6
7 8 9
'''
di = [0, 1, 0, -1]
dj = [1, 0, -1, 0]
# 입력받기
N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
# 십자가 형태로 합을 구하고 최대값 구하기

max_v = 0 # 모든 원소가 0이상이라면...
for i in range(N): # 모든 원소 arr[i][j]에 대해...
    for j in range(N):
        s = arr[i][j] # 일단 센터값으로 초기화
        for k in range(4): # 상하좌우 이동
            ni = i + di[k]
            nj = j + dj[k]
            # 배열 내부에 있으면
            if 0 <= ni < N and 0 <= nj < N:
                s += arr[ni][nj]
        # 주변원소의 합을 구하고 최댓값 찾기
        if max_v < s:
            max_v = s
