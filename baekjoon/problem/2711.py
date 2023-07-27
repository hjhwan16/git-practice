# 오타맨 고창영

T = int(input())
for i in range(T):
    l, s = map(str, input().split())
    l = int(l)
    s = s[:l-1] + s[l:]
    print(s)