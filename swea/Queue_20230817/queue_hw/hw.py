# 진기의 붕어빵
import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    N, M, K = map(int, input().split())     #N명의 손님, M초의 시간, K개의 붕어빵
    arr = list(map(int, input().split()))       #N명의 손님이 0초 이후 언제 도착하는지
    # 붕어빵이 기다림 없이 제공되면 Possible
    # 아니면 Impossible
    ans = 'Possible'

    #구현
    # 도착시간 별로 보유한 붕어빵을 리스트
    # 사람이 와서 가져가기
    # 사람이 왔을 때 붕어빵이 있는지
    Q = [0] * (max(arr) + 1)
    front = -1
    
    # 0초에 손님이 오는 경우
    if 0 in arr:
        ans = 'Impossible'
    # 1초부터 M초까지
    else:
        for sec in range(1, max(arr)+1):
            # 붕어빵 만들기
            new = 0
            if not sec % M:
                new = K
            Q[sec] = Q[sec-1] + new
            for i in arr:
                if i == sec:
                    if Q[sec] < 1:
                        ans = 'Impossible'
                    else:
                        Q[sec] -= 1
    print(f'#{tc} {ans}')

