print(ord('a')-96)
print(ord('b'))

L = int(input())
str = list(input())
s = 0
for i in range(len(str)):
    s += (31 ** (i)) * (ord(str[i]) - 96)

ans = s % 1234567891
print(ans)