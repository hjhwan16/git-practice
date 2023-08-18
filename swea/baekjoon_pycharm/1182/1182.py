# 부분집합이 아닌 부분 수열!!


def f(i, N):
    global ans
    # 부분수열이 완성이 되면
    if i == N:
        temp = 0
        for j in range(N):
            if bit[j]:
                temp += A[j]
        if temp == S:
            ans += 1
    else:
        bit[i] = 1
        f(i+1, N)
        bit[i] = 0
        f(i+1, N)
        return




N, S = map(int, input().split())
A = list(map(int, input().split()))
bit = [0] * N
ans = 0
if N == 0:
    ans = 0
    print(ans)
else:
    f(0, N)
    print(ans-1)

