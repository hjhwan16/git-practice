def fibonacci(n):
    global ans0
    global ans1
    if n == 0:
        ans0 += 1
        return 0
    elif n == 1:
        ans1 += 1
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    ans0 = 0
    ans1 = 0
    fibonacci(N)
    print(ans0, ans1)