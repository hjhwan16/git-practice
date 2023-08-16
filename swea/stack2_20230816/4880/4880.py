import sys
sys.stdin = open('input.txt')
# 싸움 붙이는 함수 list[선수번호, 패]

def match(a, b):
    # 비기는 경우
    if (a[1] == 1 and b[1] == 1) or (a[1] == 2 and b[1] == 2) or (a[1] == 3 and b[1] == 3):
        if a[0] < b[0]:
            return a
        else:
            return b
    # a가 이기는 경우
    elif (a[1] == 1 and b[1] == 3) or (a[1] == 2 and b[1] == 1) or (a[1] == 3 and b[1] == 2):
        return a

    elif (b[1] == 1 and a[1] == 3) or (b[1] == 2 and a[1] == 1) or (b[1] == 3 and a[1] == 2):
        return b


# 함수 구현 분할
def f(N, arr2):
    # 하나 남은경우 하나 반환
    if len(arr2) == 1:
        return arr2[0]
    # 계속해서 반으로 잘라 줌
    n1 = (N+1) // 2
    arr_l = arr2[:n1]
    n2 = N - n1
    arr_r = arr2[n1:]
    # print(arr_l, arr_r)
    r1 = f(n1, arr_l)
    r2 = f(n2, arr_r)
    # 경기의 결과 사라남은 사람이 반환되도록
    return match(r1, r2)


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = list(map(int, input().split()))
    #[선수번호, 패] 가 담긴 배열
    arr2 = []
    for i in range(len(arr)):
        temp = [i+1, arr[i]]
        arr2.append(temp)
    ans = 0
    # 기능 구현
    ans = f(N, arr2)[0]

    # 출력
    print(f'#{tc} {ans}')