# 20230803 / 이진탐색 / 4839

import sys
sys.stdin = open('input.txt')

# A, B 두 사람에게 교과서에서 각자 찾을 쪽 번호를 알려주면

# 이진 탐색만으로 지정된 페이지를 먼저 펼치는 사람이 이기는 게임

# 찾는 쪽 번호와 C가 같아지면 탐색을 끝냄.

# 누가 이겼는지

T = int(input())
for tc in range(1, T+1):
    # 전체쪽수 p, A가 찾아야할 쪽 pa, B가 찾아야할 쪽 pb
    p, pa, pb = map(int, input().split())
    arr = []
    for i in range(1, p+1):
        arr.append(i)
    # A 횟수
    start, end = 0, p-1
    A_cnt = 0
    # 이진 탐색
    while start <= end:
        A_cnt += 1
        center = int((start + end)/2)
        if arr[center] == pa:
            break
        elif arr[center] > pa:
            end = center
        else:
            start = center
    
    #B 횟수
    start, end = 0, p-1
    B_cnt = 0
    # 이진탐색
    while start <= end:
        B_cnt += 1
        center = int((start + end)/2)
        if arr[center] == pb:
            break
        elif arr[center] > pb:
            end = center
        else:
            start = center

    if A_cnt < B_cnt:
        ans = 'A'
    elif A_cnt > B_cnt:
        ans = 'B'
    else:
        ans = 0
    print(f'#{tc} {ans}')
