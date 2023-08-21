import sys
sys.stdin = open('input.txt')

def inorder(n):
    if n:
        inorder(ch1[n])
        print(sen[n], end = '')
        inorder(ch2[n])

T = 10
for tc in range(1, T+1):
    N = int(input())
    # 부모를 인덱스로 자식을 저장
    ch1 = [0] * (N+1)     
    ch2 = [0] * (N+1)
    # 인덱스에 해당하는 str을 저장
    sen = [0] * (N+1)

    # 입력받기
    for _ in range(N):
        arr = list(map(str, input().split()))
        p = int(arr[0])
        sen[p] = arr[1]
        if len(arr) > 2:
            for i in range(2, len(arr)):
                if ch1[p] == 0:
                    ch1[p] = int(arr[i])
                else:
                    ch2[p] = int(arr[i])
    print(f'#{tc} ', end='')
    inorder(1)
    print()

