A ,B ,C =map(int, input().split())

cnt = 0


while True:
    if B > C:
        ans = -1
        break
    else:
        cnt += 1
        cost = A + B * cnt
        if C * cnt >= cost:
            ans = cnt + 1
            break

print(ans)