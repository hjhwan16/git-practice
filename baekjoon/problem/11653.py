N = int(input())
for i in range(2, int(N/2)):
    while True:
        if N % i == 0:
            print(i)
            N = int(N / i)
        else:
            break
if N != 1:
    print(N)