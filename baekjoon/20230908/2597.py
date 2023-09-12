L = int(input())
r1, r2 = map(int, input().split())
b1, b2 = map(int, input().split())
y1, y2 = map(int, input().split())

# 빨간색 먼저 만나게 접기.
if r1 == r2:
    pass
else:
    rc = round(((r1+r2) / 2), 1)
    l1, l2 = rc, L - rc
    L = max(l1, l2)
    b1 = abs(rc - b1)
    b2 = abs(rc - b2)
    y1 = abs(rc - y1)
    y2 = abs(rc - y2)

# 길이 정하고 점 자리 갱신해주기


if b1 == b2:
    pass
else:
    bc = round(((b1+b2) / 2), 1)
    l1, l2 = bc, L - bc
    L = max(l1, l2)
    y1 = abs(bc - y1)
    y2 = abs(bc - y2)

if y1 == y2:
    pass
else:
    yc = round(((y1 + y2) / 2), 1)
    l1, l2 = yc, L - yc
    L = max(l1, l2)

print(L)