import math

T = int(input())

for i in range(T):
    a, b = map(int, input().split())
    print(int((a * b) / math.gcd(a, b)), math.gcd(a, b))