# dp를 이용해 풀어보기
N = int(input())
arr = []
for _ in range(N):
    temp = list(map(int, input().split()))
    arr.append(temp)

# 문제에서 최솟값을 출력해야 하기 때문에
# 2가지의 선택지 중에서 최솟값을 선택하여 진행
# 그러면 자동적으로 최종값은 최솟값이 되기 때문에
for i in range(1, N):
    arr[i][0] = min(arr[i-1][1], arr[i-1][2]) + arr[i][0]
    arr[i][1] = min(arr[i-1][0], arr[i-1][2]) + arr[i][1]
    arr[i][2] = min(arr[i-1][0], arr[i-1][1]) + arr[i][2]

print(min(arr[N-1]))
