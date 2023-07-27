import sys
num =int(sys.stdin.readline().rstrip())

for i in range(num):
    c, v = map(int, input().split())
    me = c // v
    dad = c % v
    print(f'You get {me} piece(s) and your dad gets {dad} piece(s).')