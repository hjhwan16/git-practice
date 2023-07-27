# 이항계수는 N개의 물건 중 K개를 순서 없이 고르는 경우의 수와 같습니다. 
# 콤비네이션 이네

def factorial(num_input):
    cnt = 1
    for i in range(1, num_input+1):
        cnt *= i
    return cnt

N, K = map(int, input().split())
print(int(factorial(N) / (factorial(K) * factorial(N - K))))