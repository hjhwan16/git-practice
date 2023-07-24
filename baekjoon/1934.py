import math
T = int(input())
for i in range(T):
    A, B = map(int, input().split())
    print(int((A * B)/(math.gcd(A, B))))
