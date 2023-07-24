# 삼각형과 세변
while True:
    a, b, c = map(int, input().split())
    my_list = [a, b, c]
    if (a == 0) and (b == 0) and (c == 0):
        break
    else:
        if max(my_list) >= (sum(my_list) - max(my_list)):
            print('Invalid')
        else:
            if a == b and b == c:
                print('Equilateral')
            elif (a == b) or (b == c) or (a == c):
                print('Isosceles')
            else:
                print('Scalene')