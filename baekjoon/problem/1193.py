# 분수 찾기
X = int(input())
tot = 0
cnt = 0
while True:
    cnt += 1
    tot += cnt
    if tot >= X:
        if cnt % 2 == 0:
        # print(cnt+1)
            print(f'{cnt - tot + X}/{tot - X + 1}')
        else:
            print(f'{tot - X + 1}/{cnt - tot + X}')
        break