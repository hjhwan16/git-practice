# 재귀를 이용한 선택 정렬

def f(i, N):
    if i == N:
        print(B)
        return
    else:
        B[i] = A[i]
        f(i+1, N)