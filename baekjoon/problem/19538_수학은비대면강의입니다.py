# 완전 탐색
# 수학은 비대면 강의입니다.
# 문자가 2개인 연립방정식을 해결하는 방법
# ax + by = c
# dx + ey = f

# 인터넷 창의 빈 칸에 수들을 입력하는 식.
# 각 칸에는 -999이상 999이하의 정수만 입력할 수 있음

a, b, c, d, e, f = map(int, input().split())

for i in range(-999, 1000):
    for j in range(-999, 1000):
        if (a * i + b * j == c) and (d * i + e * j == f):
            print(i, j)