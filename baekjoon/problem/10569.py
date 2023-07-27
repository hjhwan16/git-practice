import sys
num = int(sys.stdin.readline().rstrip())
for i in range(num):
    V, E = map(int, input().split())
    print(2 - V + E)