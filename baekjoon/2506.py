cnt = 0
tot = 0
N = int(input())
my_lst = list(input().split())
#print(my_lst)

for i in range(N):
    if my_lst[i] == '0':
        cnt = 0
        #print(cnt)
    else: 
        cnt += 1
        #print(cnt)
        tot += cnt

print(tot)
