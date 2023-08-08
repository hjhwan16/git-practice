C = int(input())
for tc in range(1, C+1):
    arr = list(map(int, input().split()))
    total = 0
    num = arr[0]
    for i in arr[1:]:
        total += i
    ave = total / num
    count = 0
    for k in arr[1:]:
        if k > ave:
            count += 1
    print(f'{(count/num)*100:.3f}%')