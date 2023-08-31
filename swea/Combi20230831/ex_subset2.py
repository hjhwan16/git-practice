# 부분집합 합 문제 구하기
# 10개의 정수 집합에 대한 모든 부분 집합 중 원소의 합이 0이 되는 경우
# 누적합을 함께 전달
# 갯수까지 함께 전달 -> 공집합 제외 방법
def subset(i, N):
    if i == N:

        for j in range(N):
            if bit[j]:
                print(arr[j], end= ' ')
        print()
    else:
        bit[i] = 1
        subset(i+1, N)
        bit[i] = 0
        subset(i+1, N)


arr = [-1, 3, -9, 6, 7, -6, 1, 5, 4, -2]
N = len(arr)
bit = [0] * N
subset(0, N)