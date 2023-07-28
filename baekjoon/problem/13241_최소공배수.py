# 최소공배수
# 유클리드 호제법으로 최대공약수(최소공배수)를 빠르게 구하는 문제
# 유클리드 호제법이란? 나머지로 계속해서 나누는 방법
# 그러다가 나누어 떨어지면 그것이 최대 공약수

A, B = map(int, input().split())

# A가 큰 조건으로 만들어 주기
while True:
    if A < B:
        A, B = B, A
    m = A // B
    n = A % B

    if n == 0:
        print(m)
        break
    
    else:
        A = n
        B = m
