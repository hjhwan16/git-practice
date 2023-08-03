# 20230803 / 4837번 / 부분집합의 합
import sys
sys.stdin = open('input.txt')

# 1부터 12까지의 숫자를 원소로 가진 집합 A
# 집합 A의 부분집합 중 N개의 원소를 갖고 있고, 원소의 합이 K인 부분집합의 개수를 출력
# 해당하는 부분집합이 없는 경우 0을 출력
arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]

T = int(input())
for tc in range(1, T+1):
    N, K = map(int, input().split())
    # 조건을 만족하는 부분집합의 개수
    ans = 0
    # 부분집합 만들기
    for i in range(1, 1 << 12): # 공집합을 제외
        # 부분집합의 합 초기화
        tot_temp = 0
        # 부분집합의 원소의 수 초기화
        cnt = 0
        for j in range(12):
            if i & (1 << j):
                tot_temp += arr[j]
                cnt += 1
                # print(arr[j], end=' ')
        # 주어진 조건과 부합하면 ans 1씩 증가
        if cnt == N and tot_temp == K:
            ans += 1
        # print()

    print(f'#{tc} {ans}')