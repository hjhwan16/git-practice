import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = []
    for _ in range(N):
        temp_list = list(map(int, input().split()))
        arr.append(temp_list)
    # print(arr)
    arr.sort(key=lambda x:x[1])     # 종료시간 기준으로 정렬
    # 초기 상태를 만들어 줌
    arr =[[0, 0]] + arr
    # print(arr)

    S = []  # 활동의 종료시간
    j = 0
    ans = 0

    for i in range(1, N+1):
        if arr[i][0] >= arr[j][1]: #si vs fj
            S.append(i)
            j = i # 마지막 활동 최신화
            ans += 1
    # print(S)
    print(f'#{tc} {ans}')