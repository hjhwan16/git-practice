import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())    # N개의 컨테이너, M개의 트럭
    w_lst = list(map(int, input().split()))
    t_lst = list(map(int, input().split()))
    w_lst.sort(reverse=True)
    t_lst.sort(reverse=True)
    # print(w_lst)
    # print(t_lst)
    ans = 0
    cnt = 0
    for i in range(M):
        for j in range(cnt, N):
            cnt += 1    # 화물을 넘어갈 때 마다 하나 씩 증가 후 그 지점 이후부터 탐색
            if t_lst[i] >= w_lst[j]:
                # print(i, j)
                # print(t_lst[i], w_lst[j])
                ans += w_lst[j]     #그리디로 실을 수 있는 최고의 무게를 적재
                break
    print(f'#{tc} {ans}')
