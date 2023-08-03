import sys
sys.stdin = open('input.txt')
# 0~9 사이의 숫자 카드에서 임의의 카드 6장을 뽑음
# 3장의 카드가 연속적인 번호를 갖는 경우 run
# 3장의 카드가 동일한 번호를 갖는 경우 triplet
# 6장의 카드가 run과 triple로만 구성된 경우 baby gin
# baby gin 여부 판단 프로그램

T = int(input())
for tc in range(1, T+1):
    num = int(input())
    cnt_arr = [0] * 12

    # 카운팅 정렬 사용
    for i in range(6):
        cnt_arr[num % 10] += 1
        num //= 10
    # triple이 있는지 확인 -> run이 있는지 확인
    triple = 0
    run_cnt = 0
    for i in range(10):
        # triple 있는지 확인
        if cnt_arr[i] == 3:
            # print('triple')
            cnt_arr[i] = 0
            triple += 1

        elif cnt_arr[i] == 6:
            cnt_arr[i] = 0
            triple += 2

        for k in range(10):
            if (cnt_arr[k] >= 1) and (cnt_arr[k+1] >= 1) and (cnt_arr[k+2] >= 1):
                # print('run')
                run_cnt += 1
                cnt_arr[k] -= 1
                cnt_arr[k+1] -= 1
                cnt_arr[k+2] -= 1
                # print(cnt_arr)
    if triple + run_cnt == 2:
        ans = 1
    else:
        ans = 0
    print(f'#{tc} {ans}')
