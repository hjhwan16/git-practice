import math

N, M, K = map(int, input().split())
if K == 0:
    i,j = 0,0
else:
    i = (K-1) // M
    j = (K-1) % M
# print(i,j)
ans1 = math.factorial(i+j)//(math.factorial(i)*math.factorial(j))
ans2 = math.factorial(N+M-i-j-2)//(math.factorial(N-i-1)*math.factorial(M-j-1))
# print(ans1, ans2)
print(ans1 * ans2)