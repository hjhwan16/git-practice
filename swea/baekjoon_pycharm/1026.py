# 보물 / 20230901
N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
# A의 가장 큰수와 B의 가장 작은수를 곱해줘야 함.

A.sort()
B.sort(reverse=True)
s = 0
for i in range(N):
    s += A[i] * B[i]
print(s)