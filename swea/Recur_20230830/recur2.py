# 재귀를 이용한 선택 정렬
# key가 있으면 1, 없으면 0을 리턴하는 함수
def f(i, N, key, A):
    if i == N:
        return 0
    elif A[i] == key:
        return 1
    else:
        return f(i+1, N, key, A)

N = 5
A = [1, 2, 3, 4, 5]
key = 10
print(f(0, N, key, A))