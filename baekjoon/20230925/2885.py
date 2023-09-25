# 그리디 알고리즘

# K 보다 작은 2의 제곱수를 빼가면서 0을 만들기

K = int(input())
num = 1
cnt = 0
while True:
    temp = 2 ** (cnt)
    if temp >= K:
        break
    cnt += 1
ans = 0 + temp
ans2 = 0
while True:
    if K == 0:
        break
    if temp <= K:
        K -= temp
    temp = temp // 2
    ans2 += 1


print(ans, ans2-1)