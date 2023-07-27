for i in range(3):
    lst = []
    lst = list(map(int, input().split()))
    tot = sum(lst)
    if tot == 4:
        print("E")
    elif tot == 3:
        print("A")
    elif tot == 2:
        print("B")
    elif tot == 1:
        print("C")
    else:
        print("D")