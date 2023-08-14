# 직사각형을 만드는 방법
n = int(input())
ans = 0

for i in range(1, int(n**(1/2))+1):
    for k in range(i, (n//i)+1):
        ans += 1

print(ans)