# 세 수가 연속해서 주어졌을 때 한 번의 곱셈 기호와 한 번의 나눗셈 기호를 이용하여 만든 식 중 가장 큰 값을 출력하는 프로그램

A, B, C = map(int, input().split())

ans_1 = int(A * B / C)
ans_2 = int(A / B * C)

if ans_1 >= ans_2:
    ans = ans_1
else:
    ans = ans_2

print(ans)