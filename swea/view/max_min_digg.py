# extra 최대 최소의 간격
# N개의 양의 정수가 첫번째 부터 N까지 주어짐.
# 최대값의 위치와 최소값의 위치의 차이를 절대값으로 출력
# 가장 작은 수가 여러개인 경우 -> 먼저 나오는 위치
# 가장 큰 수가 여러개인 경우 -> 마지막으로 나오는 위치
import sys
sys.stdin = open('input.txt')
# 테스트 케이스
T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = list(map(int, input().split()))
    max_v = arr[0]
    max_idx = 0
    min_v = arr[0]
    min_idx = 0
    # 배열 입력받기
    # 배열을 순회하며 최댓값과 최소값 찾기
    for i in range(len(arr)):
        if max_v <= arr[i]:
            max_v = arr[i]
            max_idx = i
        if min_v > arr[i]:
            min_v = arr[i]
            min_idx = i
    # 차이 출력
    ans = max_idx - min_idx
    if ans < 0:
        ans *= -1

    print(f'#{tc} {ans}')

