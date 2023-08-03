N = 2 # 행의크기
M = 4 # 열의크기
arr = [[0, 1, 2, 3], [4, 5, 6, 7]]
# 행우선탐색
for i in range(N):
    for j in range(M):
        print(arr[i][j])
# 열우선탐색
for j in range(M):
    for i in range(N):
        print(arr[i][j])
# 지그재그탐색1
for i in range(N):
    for j in range(M):
        print(arr[i][j + (M-1-2*j) * (i%2)])
# 비어있는 배열 만들기
N = 2
M = 4
arr1 = [[0]*M for _ in range(N)]
# 리스트 복사: for문 사용해서 하나하나 복사