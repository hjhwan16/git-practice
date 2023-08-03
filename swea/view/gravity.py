import sys
sys.stdin = open('input.txt')

T = int(input())#테스트 케이스
for tc in range(1, T+1):
    N = int(input())#방의 가로길이
    arr = list(map(int, input().split()))#쌓여 있는 상자의 수
    ans = 0
    max_v = 0
    for i in range(len(arr)):# arr 을 돌면서 자기와 같거나 큰 값을 찾음
        cnt = 0
        for k in range(i+1, len(arr)): #그 뒤로 작은 값이 있을 때 cnt를 하나씩 증가 시키기
            if arr[i] > arr[k]:
                cnt += 1
        if cnt >= ans: # cnt 가 ans 보다 크다면 cnt를 max로 바꿔 줌.
            ans = cnt
    print(f'#{tc} {ans}')