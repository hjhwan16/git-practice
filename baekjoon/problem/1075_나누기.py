# 나누기
# 완전 탐색
# N과 F가 주어짐 N 뒤에 두자리를 적절히 바꿔 N을 F로 나누어 떨어지게 만들려고 한다.
# 만약 가능하다면 두 두자리를 가능한 작게 만들려고 함

# N = 275 -> F = 5 라면 200 200이 가장 작은 5로 나누어 떨어지는 수

N = int(input())
F = int(input())

new_num = int(str(N)[:-2] + '00')

# print(int(str(N)[:-2] + '00'))

for i in range(100):
    check_num = new_num + i
    # print(check_num)
    if check_num % F == 0:
        print(str(check_num)[-2:])
        break