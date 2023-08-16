# f(i, N, s): s: i-1 단계까지의 부분집합의 합

# 부분집합의합 구하기 / 재귀2

def f(i, N, s): # s: i-1 원소까지의 합(포함된 원소의 합)
    if i == N:
        print(bit, end = ' ')
        print(f': {s}')
        return
    else:
        bit[i] = 1 # A[i]가 포함이 되는 경우
        f(i+1, N, s+A[i])
        bit[i] = 0 # A[i]가 포함되지 않는 경우
        f(i+1, N, s)
        return

A = [1, 2, 3]
bit = [0]*3
f(0, 3, 0)


