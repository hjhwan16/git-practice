import sys
sys.stdin = open('input.txt')
# 20230808 / str

# 문자열 A를 타이핑 하려고 한다.
# 한 글자 씩 타이핑 하려면 A의 길이만큼 키를 눌러야 함.
# 문자열 B가 저장되어 있어서 키를 한번 누른 것으로 B전체를 타이핑 할 수 있다.
# 이미 타이핑 한 문자를 지우는 것은 불가능하다.
# A와 B가 주어질 때 A 전체를 타이핑 하기 위해 키를 눌러야 하는 횟수의 최솟값을 구하라.

T = int(input())

for tc in range(1, T+1):
    ans = 0
    cnt = 0

    target, pattern = map(str, input().split())
    # 동일하다면 빼고
    # 이제 동일하지 않다면 나머지 길이 더하기
    m = len(target)
    n = len(pattern)
    i = 0 # target의 idx
    j = 0 # pattern의 idx
    while i < m:
        if target[i] != pattern[j]:
            i = i - j
            j = -1
        i += 1
        j += 1
        # 하나 찾으면 cnt 하나씩 증가 j 0으로 초기화
        if j == n:
            cnt += 1
            j = 0
    # 계산
    ans = cnt + (m-cnt*n)
    print(f'#{tc} {ans}')