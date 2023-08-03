import sys
sys.stdin = open('input.txt')

T = int(input()) #테스트케이스
for tc in range(1, T+1):
    N = int(input())
    arr = list(map(int, input().split()))

    min_idx = 0 #최솟값의 인덱스
    max_idx = 0 #최댓값의 인덱스
    for i in range(1, N):
        # 같은애가 나오는 경우 갱신x 갱신하고 싶으면 등호를 포함시키면 됨.
        if arr[min_idx] > arr[i]: #먼저나오는 경우
            min_idx = i #i로 갱신
        # 최댓값은 같은 수가 나오는 경우 마지막으로 나오는 위치로 함.
        if arr[max_idx] <= arr[i]:
            max_idx = i #i로 갱신
    if max_idx > min_idx:
        ans = max_idx - min_idx
    else:
        ans = min_idx - max_idx

    print(f'#{tc} {ans}')