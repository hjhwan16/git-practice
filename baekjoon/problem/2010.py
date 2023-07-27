import sys
num = int(sys.stdin.readline().rstrip())
total = 1

for i in range(num):
    cnt = int(sys.stdin.readline().rstrip())
    total = total + cnt -1

print(total)