# 이분탐색 / K 번째 수

# N * N 배열 A 를 만듦

# A[i][j] = i * j 이다.

# 이 수를 일차원 배열 B에 넣으면 N의 크기는 N*N이 된다.

# B를 오름차순 정렬하고 B[k]를 구해보자

# 배열 A와 B의 인덱스는 1부터 시작한다

N = int(input())
k = int(input())
B = []
count = 0
for i in range(1, N+1):
    temp_count = int(i ** 2)
    if k < temp_count:
        count = i

print(count)
