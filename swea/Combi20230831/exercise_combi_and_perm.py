a = [1, 2, 3, 4, 5]
N = 5
R = 3
tr = [0] * R
used = [0] * N
p = [0] * R

def nCr(n, r):
    if r == 0:
        print(tr)
    elif n < r:
        return
    else:
        tr[r-1] = a[n-1]
        nCr(n-1, r-1)
        nCr(n-1, r)

def nPr(i, k, N):
    if i == k:
        print(p)
        return
    else:
        for j in range(N):
            if used[j] == 0:
                p[i] = a[j]
                used[j] = 1
                nPr(i+1, k, N)
                used[j] = 0

nPr(0, R, N)
print('_________')
nCr(N, R)