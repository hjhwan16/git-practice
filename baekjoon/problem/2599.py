# 10일간의 온도가 주어짐.
# 연속적인 K일의 온도의 합이 최대가 되는 값을 출력
import sys
input = sys.stdin.readline

N, K = map(int, input().split())

arr = list(map(int, input().split()))

max_v = 0

for i in range(N-K+1):
    temp = 0
    for k in range(K):
        temp += arr[i+k]
    if max_v < temp:
        max_v = temp

print(max_v)

# 시간초과