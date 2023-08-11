import sys
sys.stdin = open('input.txt')

# 조건 하에 사재기를 해 최대한 이득 취하기

# 1. 연속된 N일 동안의 물건의 매매가를 예측하여 알고 있음
# 2. 당국의 감시망에 걸맂 않기 위해 하루에 최대 1만큼 구매할 수 있음
# 3. 판매는 얼마든지 할 수 있다.

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    ans = 0
    # max 값이 아니면 사야함
    # cnt 보유 갯수
    cnt = 0
    cost = 0
    # 각 경우마다 팔면서 max_profit을 찾기
    arr = list(map(int, input().split()))
    max_v = max(arr)
    for i in arr:
        if i < max_v:
            cnt += 1
            cost += i
        if i == max_v:
            profit = (i * cnt) - cost

        # 팔아서 얻는 수익은?
        profit = (i * cnt) - cost
        if ans < profit:
            ans = profit

    print(f'#{tc} {ans}')