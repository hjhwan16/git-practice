# N = int(input())
# n_lst=[]
# n_lst.append(N)
# n_lst.append(1)
# for i in range(2, int(N/2)+1):
#     if N % i == 0:
#         n_lst.append(i)
        
# print(n_lst)

while True:
    num = int(input())
    if num == -1:
        break
    else:
        num_lst=[num]
        for i in range(1, int(num/2)+1):
            if num % i == 0:
                num_lst.append(i)
        #print(num_lst)
    
    if num_lst[0] == sum(num_lst[1::]):
        print(num_lst[0], '=', end=' ')
        for k in range(1, len(num_lst)-1):
            print(num_lst[k], '+', end=' ')
        print(num_lst[-1])
    else:
        print(num_lst[0], "is NOT perfect.")