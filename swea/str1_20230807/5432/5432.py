import sys
sys.stdin = open('input.txt')

# 쇠막대기 # 스트링 # 20230807

# 레이저 하나가 쇠막대기 하나와 만날때마다 갯수는 하나씩 증가.

# 몇개의 쇠막대기가 있고 이게 레이저랑 몇번 만나는지?

# ()이 ((((몇개 다음 나오는지를 확인하면?

# (이 나오면 cnt 하나 증가 ) 이 나오면 cnt 하나감소

# ()를 만나면 total += cnt

# 전체 갯수 새기 iorn += 1 ()가 아닌 (를 만날 때

T = int(input())
for tc in range(1, T+1):
    word = str(input())
    len_word = len(word)
    # 최초 막대기 갯수
    iorn = 0
    laser = 0
    total = 0
    cnt = 0
    for i in range(len_word-1):
        # 최초 막대기 갯수
        if word[i] == '(' and word[i+1] != ')':
            iorn += 1
            # cnt 증가
            cnt += 1
        # laser 갯수
        if word[i] == '(' and word[i+1] == ')':
            total += cnt
            laser += 1
        # 닫히면 cnt 감소
        if word[i] == ')' and word[i-1] != '(':
            cnt -= 1
    ans = total + iorn
    print(f'#{tc} {ans}')