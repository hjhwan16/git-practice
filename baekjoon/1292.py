# 쉽게 푸는 문제
tot = 0
mul = 0
cnt = 1
num_list = []
A, B = map(int, input().split())
while True:
    if mul >= B:
        break
    mul = int((cnt * (cnt + 1))/2)
    tot = tot + mul
    # print(mul, cnt)
    for i in range(cnt):
        num_list.append(cnt)
    cnt += 1
print(sum(num_list[A-1:B]))