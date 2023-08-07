import sys
sys.stdin = open('input.txt')


T = int(input())
for tc in range(1, T+1):
    ans = ''
    # 2차원 배열 받기 # max len 찾으면서
    arr = []
    max_len = 1
    for _ in range(5):
        temp = list(str(input()))
        arr.append(temp)
        if max_len < len(temp):
            max_len = len(temp)
    
    # max len으로 통일 시켜주기 위해 ''를 추가해줌
    for k in arr:
        for l in range(max_len-len(k)):
            k.append('')
    
    # 열방향으로 돌면서 하나씩 더해줌
    for j in range(max_len):
        for i in range(5):
            ans += arr[i][j]

    print(f'#{tc} {ans}')