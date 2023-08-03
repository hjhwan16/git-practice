import sys
sys.stdin = open('input.txt')

# 왼쪽과 오른쪽으로 창문을 열었을 때, 양쪽 모두 거리 2 이상의 공간이 확보될 때 조망권이 확보

# 조망권이 확보된 세대의 수를 반환하는 프로그램을 작성


for tc in range(1, 11):
    N = int(input()) #건물의 갯수
    arr = list(map(int, input().split())) #N개의 건물의 높이
    ans = 0
    for i in range(2, N-1): # 3부터 98
        for k in range(1, arr[i]+1):# i번째 빌딩의 높이 0 1층 부터 225층까지 올라감
            if (k > arr[i-2]) and (k > arr[i-1]) and (k > arr[i+1]) and (k > arr[i+2]):
                ans += 1
    print(f'#{tc} {ans}')
