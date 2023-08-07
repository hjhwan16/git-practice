# 재석이는 호수판 제작업체의 직원
# 숫자와 숫자 사이 여백
# 왼쪽 오른쪽으로 여백
# 규칙은 간단
# 각 숫자 사이에는 1cm 여백
# 1은 2cm의 너비를 차지
# 0은 4cm / 나머지는 3cm
# 좌우 경계 1cm 여백

while True:
    N = int(input())
    if N == 0:
        break
    ans = 0
    
    len_n = len(str(N))
    ans += len_n - 1

    for i in range(len_n):
        n = N % 10
        N = N // 10
        if n == 0:
            print('0')
            ans += 4
        elif n == 1:
            print('1')
            ans += 2
        else:
            print('others')
            ans += 3

    ans += 2
    print(ans)


