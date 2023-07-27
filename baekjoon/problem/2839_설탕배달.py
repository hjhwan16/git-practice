# 완전탐색
# 설탕배달
# 사탕가게에 설탕을 정확하게 N킬로그램 배달해야 함.
# 설탕은 봉지에 담겨져 있음
# 봉지는 3, 5킬로그램 존재
# 최대한 적은 봉지를 이용해 가려함.
# 정확하게 N 킬로그램 배달해야 할 때, 봉지를 몇개 가져가야 되는 지?

N = int(input())
max_three = N // 3
max_five = N // 5
num_list = []

for t in range(0, max_three + 1):
    for f in range(0, max_five + 1):
        if 3 * t + 5 * f == N:
            num_list.append(t + f)

if len(num_list) == 0:
    print(-1)
else:
    print(min(num_list))


