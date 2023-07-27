# 큰 일직선 모양의 강이 흐르고 있음. 다리가 없음
# 서쪽에 N개의 사이트, 동쪽에 M개의 사이트
# 서쪽과 동쪽의 다리를 연결하고자함, 서쪽의 사이트 만큼 다리를 연결 다리를 지을 수 있는 경우의 수는?
# M개중 N개를 고르는 경우

def factorial(num_input):
    cnt = 1
    for i in range(1, num_input+1):
        cnt *= i
    return cnt

T = int(input())
for i in range(T):
    N, M = map(int, input().split())
    print(int(factorial(M) / (factorial(N) * factorial(M - N))))