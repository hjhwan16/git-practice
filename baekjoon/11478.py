# 서로 다른 부분 문자열의 개수
S = str(input())
word_set = set()

for i in range(len(S)): #0,1,2,3,4
    end_point = (len(S)) - i
    for k in range(end_point):
        # print(i,k)
        # print()
        word_set.add(S[k : (k + i + 1)])

print(len(word_set))    