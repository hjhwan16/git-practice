import sys
sys.stdin = open('input.txt')
T = int(input()) #테스트 케이스
for tc in range(1, T+1):
    N = int(input()) #수열의 길이
    arr = list(map(int, input())) #수열
    max_v = 0
    cnt = 0
    #1이 연속할 때 카운팅 해주고 그 카운팅의 max값을 찾아야 함.
    for i in range(N):
        if arr[i] == 0:
            cnt = 0
        elif arr[i] == 1:
            cnt += 1
            if cnt > max_v:
                max_v = cnt
    ans = max_v
    print(f'#{tc} {ans}')