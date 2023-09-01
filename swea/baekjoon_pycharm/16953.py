# A -> B / 20230901
# 거꾸로
A, B = map(int, input().split())
cnt = 1
while True:
    if B <= A:
        if B == A:
            print(cnt)
        else:
            print(-1)
        break

    if B % 10 == 1:
        B = B // 10
        # print(B)
        cnt += 1
    elif B % 2 == 0:
        B = B // 2
        # print(B)
        cnt += 1
    else:
        print(-1)
        break