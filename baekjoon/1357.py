# 뒤집힌 덧셈
def Rev(num):
    return int(str(num)[::-1])

X, Y = map(int, input().split())

print(Rev(Rev(X) + Rev(Y)))
