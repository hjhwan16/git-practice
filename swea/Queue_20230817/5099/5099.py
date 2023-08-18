import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    # 피자의 갯수 M개
    arr = list(map(int, input().split()))
    idx = 0
    ans = 0
    cnt = 0 # 빼는 피자의 갯수

    # 화덕의 자릿수 N
    Q = [] # N 길이의 큐 생성 [치즈, 피자번호]
    front = 0
    result = []
    for _ in range(N):
        Q.append([0, 0])

    while True:
        # 화덕이 비고 피자가 남았다면? 투입하고 돌리기
        if Q[front][1] == 0 and idx <= M-1:
            Q[front] = [arr[idx], idx+1]
            idx += 1
            front = (front + 1) % N
            # print('투입', Q)

        # 화덕이 비지 않았다면? 치즈 덜고 체크하기
        else:
            # 치즈 덜기
            Q[front][0] = Q[front][0] // 2
            # 0이 되면 빼기
            if Q[front][0] == 0 and Q[front][1] != 0:
                result.append(Q[front][1])
                Q[front] = [0, 0]
                cnt += 1
                # 피자가 M-1개 빠져나갔다면 끝냄
                if cnt == M:
                    # print('끝', Q, front)
                    break
                # 빼고 피자가 남았다면 투입
                if idx <= M-1:
                    Q[front] = [arr[idx], idx + 1]
                    idx += 1

            front = (front + 1) % N
            # print('else', Q)

    print(f'#{tc} {result[-1]}')


