def is_groupword(word):
    word_list = list(word)
    #print("1",word_list)
    temp=[]
    temp.append(word_list.pop())
    while True:
        
        if len(word_list)==0:
            #print("The end")
            answer = 1 
            break
        #print("2",word_list, temp)
        if word_list[-1]==temp[-1]:
            word_list.pop()
        else: 
            if word_list[-1] in temp:
                answer = 0 
                break
            else:
                temp.append(word_list.pop())
    return answer
    
N = int(input())
count = 0
for i in range(N):
    words = str(input())
    count += is_groupword(words)
print(count)

    


