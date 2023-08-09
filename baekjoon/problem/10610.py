# 30의 배수인지

N = list(str(input()))
arr = list(map(int, N))
# print(arr)
# 배열에 담기
# 담으면서 0이 있는지
# 합이 3의 배수인지 확인
isThree = False
isZero = False
ans = 0

if 0 in arr:
    isZero = True

# 합이 3의 배수인지
if sum(arr) % 3 == 0:
    isThree = True

if isZero and isThree:
    arr.sort(reverse=True)
    for i in arr:
        print(i, end='')
else:
    print(-1)

