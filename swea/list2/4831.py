# 전기버스
import sys
sys.stdin = open('input.txt')
import copy

# 전기버스는 한번 충전으로 이동할 수 있는 정류장 수가 정해짐
# 중간에 충전기가 설치된 정류장을 만듦.
# 0번에서 출발해 종점인 N번 정류장까지 이동
# 한번 충전으로 이동할 수 있는 정류장 수 K
# 충전기가 설치된 M개의 정류장 번호
# 최소한 몇 번의 충전을 해야 종점에 도착할 수 있는지 출력하는 프로그ㅐㅁ
# 종점에 도착할 수 없는 경우 0을 출력
# 출발지에는 항상 충전기가 설치 but 충전횟수에 포함x

T = int(input()) #노선 수
for tc in range(1, T+1):
    K, N, M = map(int, input().split()) #한번 충전 후 이동정류장 수 , 정류장 수, 충전기 갯수
    arr = list(map(int, input().split())) # 충전기 위치
    arr1 = [0] * (N + K + 1)
    # 시작점과 끝지점은 충전기가 있다고 두고 시작
    arr1[0] = 1
    arr1[N:] = [1] * K
    # 정류장0 시작점 -> 0인 곳은 충전기 없음 -> 1인 곳은 충전기 있음
    for i in arr:
        arr1[i] = 1 # [0, 1, 0 ,1, 0, 1, 0, 1, 0, 1, 0]

    # 도착할 수 있는가?
    fuel = 0 + K
    ans = 0

    for k in range(N):
        # 시작점은 항상 풀충
        if k == 0:
            fuel = 0 + K
            # print(k, fuel)
            fuel -= 1
        # 1이면 충전
        elif arr1[k] == 1:
            # 충전기에 도착했는데 연료가 0이거나 남은 거리에 충전소가 없다면 충전
            if (fuel == 0):
                fuel = 0 + K
                # print(k, '0충전')
                ans += 1
                fuel -= 1
            # 남은 연료 거리 안에 충전소가 없다면 층전
            elif not(1 in arr1[k+1: k+fuel+1]):
                # print(arr1[k+1: k+fuel+1])
                # print(k, '1충전')
                fuel = 0 + K
                ans += 1
                fuel -= 1
            # 남은 연료 거리 안에 충전소가 있으면 keep going
            else:
                # print(k, fuel)
                fuel -= 1
        # 아니면 연료 소모
        else:
            # 충전기가 없는데 연료가 0이 되면 멈춤.
            if fuel <= 0:
                ans = 0
                break
            fuel -= 1

    print(f'#{tc} {ans}')