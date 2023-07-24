# 세탁소 사장 동혁
coin =[25, 10, 5, 1]
T = int(input())

for _ in range(T):
    price = int(input())
    coin_list = []
    for i in coin:
        if (price // i) >= 1:
            coin_list.append(price // i)
            price = price - i * (price // i)
        else:
            coin_list.append(0)
    for k in coin_list:
        print(k, end=' ')
    print()


