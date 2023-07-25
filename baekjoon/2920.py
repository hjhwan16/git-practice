list1 = list(map(int, input().split()))

if list1 == sorted(list1):
    print('ascending')
elif list1 == sorted(list1, reverse=True):
    print('descending')
else:
    print('mixed')