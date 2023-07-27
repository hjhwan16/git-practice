#직각 삼각형

while True:
    a, b, c = map(int, input().split())
    if a == 0 and b == 0 and c == 0:
        break
    else:
        num_list = [a, b, c]
        num_list.sort()
        if num_list[-1] ** 2 == num_list[0] ** 2 + num_list[1] ** 2:
            print('right')
        else:
            print('wrong')
        