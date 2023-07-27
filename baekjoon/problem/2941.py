croatian = ["c=","c-","dz=","d-","lj","nj","s=","z="]
words = str(input())
cnt_lst=[]

for i in croatian:
    count = words.count(i)
    #print(count)
    cnt_lst.append(count)

cnt_lst[7]-=cnt_lst[2]
#print(cnt_lst)

final_count = len(words)-sum(cnt_lst)-cnt_lst[2]
print(final_count)