case = int(input())
for i in range(case):
    total = 0
    price = int(input())
    total += price
    num = int(input())
    for k in range(num):
        q, p = map(int, input().split())
        total += q * p
    print(total)
        
