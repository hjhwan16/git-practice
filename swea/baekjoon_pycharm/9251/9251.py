import sys
sys.stdin = open('input.txt')

str1 = list(input())
str2 = list(input())
l1 = len(str1)
l2 = len(str2)

idx1 = 0
idx2 = 0

ans = 0

while idx1 < l1:
    for i in range(idx1, l1):
        for j in range(idx2, l2):
            if str1[i] == str2[j]:
                ans += 1
                str2[idx2], str2[j] = str2[j], str2[idx2]
                idx2 += 1
                str1[idx1], str1[i] = str1[i], str1[idx1]
                idx1 += 1
                break
        else:
            str1[idx1], str1[i] = str1[i], str1[idx1]
            idx1 += 1
            break

print(ans)