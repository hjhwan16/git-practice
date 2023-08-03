# 행열 탐색 연습

# 0으로 초기화 된 N * M의 2차원 배열 생성하기.
m = 3
n = 3

arr = []
for i in range(n):
    row = [0] * m
    arr.append(row)
print(arr)

# 행 우선 순회를 다른 것보다 우선시 하여 학습하자!
num_list = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print(num_list)

# 1. 행 우선 순회 정상적으로 진행되는지 확인
for r in range(len(num_list)):
    for c in range(len(num_list[0])):
        print(f'{num_list[r][c]}', end=' ') # 1 2 3 4 5 6 7 8 9
print()

# 2. 열 우선 순회
for c in range(len(num_list[0])):
    for r in range(len(num_list)):
        print(f'{num_list[r][c]}', end=' ') # 1 4 7 2 5 8 3 6 9
print()

# 3. 역-행 우선 순회
for i in range(n):
    for j in range(m-1, -1, -1):
        print(num_list[i][j], end=' ') # 3 2 1 6 5 4 9 8 7
print()

# 4. 역-열 우선 순회
for j in range(m):
    for i in range(n-1, -1, -1):
        print(num_list[i][j], end=' ') # 7 4 1 8 5 2 9 6 3
print()

# 5. 가장자리의 합
def edge_sum(arr):
    # 순회를 하면서, 2차원 리스트의 가장자리에 있는 원소들을 합한다.
    edge_sum_result = 0
    for i in range(len(arr)):
        for j in range(len(arr[0])):
            if (i == 0) or (i == len(arr) -1) or (j == 0) or (j == len(arr[0]) - 1):
                # print(arr[i][j])
                edge_sum_result += arr[i][j]

    return edge_sum_result


result = edge_sum(num_list)
print(result) # 40

# 6. 델타 탐색
# 탐색 순서는 주어진 조건에 맞춰서 구현해야 한다.
        # 상 하 좌 우
d_row = [-1, 1, 0, 0]
d_col = [0, 0, -1, 1]
# 대각선
       # 좌상단 / 좌하단 / 우상단 / 우상단
dxy = [(-1, -1), (-1, 1), (1, -1), (1, 1)]

# 벽을 세워야 한다. = 주어진 2차원 리스트의 범위를 벗어나지 않도록 제한을 두는 행위
# 1. 벽에 제한을 두는 데, 벽을 넘어가는 경우, 아무것도 하지 않는다.
# 2. 벽을 넘어가지 않는 경우에만 기능을 수행한다.
x = 0
y = 1
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
N = 5
for d in range(4):
    # 다음에 탐색할 좌표 담기.
    nx = x + dx[d]
    ny = y + dy[d]

    # 바뀐 좌표가 map을 벗어나는지 확인.
    if nx < 0 or nx >= N or ny < 0 or ny >=N:
        # map을 벗어나는 경우 일로 들어옴.
        continue

    # map을 벗어나지 않는 경우
    if 0 <= nx < N and 0 <= ny < N:
        # map을 벗어나지 않는 경우 일로 들어옴.
        continue

def isSafeArea(nx, ny, N):
    if 0 <= nx < N and 0 <= ny < N:
        # map을 벗어나지 않는 경우 일로 들어옴.
        return True
    return False


