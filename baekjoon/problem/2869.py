# 달팽이는 올라가고 싶다.
A, B, V = map(int, input().split())
# y = 0
# cnt = 0
# while True:
#     cnt += 1
#     y = y + A
#     if y >= V:
#         break
#     y = y - B
# print(cnt)

V = V - A

if (V % (A-B)) == 0: 
    print(V // (A-B) + 1)
else:
    print(V // (A-B) + 2)