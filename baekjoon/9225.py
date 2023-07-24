import sys
num = int(sys.stdin.readline().rstrip())
for i in range(num):
    a1, a2 = map(int, input().split())
    print(f'Case {i+1}: {a1+a2}')