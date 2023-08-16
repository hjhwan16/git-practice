# 거듭제곱
def f1(b, e):
    if b == 0:
        return 1
    r = 1
    for i in range(e):
        r *= b
    return r

def f2(b, e):
    if b == 0 or e == 0:
        return 1
    r = 1
    if e % 2: # 홀수라면
        r = f2(b, (e-1)//2)
        return r*r*b
    else:
        r = f2(b, e//2)
        return r*r