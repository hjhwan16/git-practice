# extra / 연속한 1의 개수
# N개의 0과 1로 이루어진 수열에서 연속한 1의 개수 중 최대값을 출력하시오.
import sys
sys.stdin = open('input.txt')


T = int(input())

for tc in range(1, T+1):
    N = int(input())
    arr = list(map(int, input()))
    max_v = 0
    cnt = 0
    for i in arr:
        if i == 0:
            cnt = 0
        elif i == 1:
            cnt += 1
            if max_v <= cnt:
                max_v = cnt
    print(f'#{tc} {max_v}')