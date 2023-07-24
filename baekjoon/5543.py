b1 = int(input())
b2 = int(input())
b3 = int(input())
d1 = int(input())
d2 = int(input())

burgers = [b1, b2, b3]
drinks = [d1, d2]

burgers.sort()
drinks.sort()

print(burgers[0] + drinks[0] - 50)
