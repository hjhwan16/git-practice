# ROT13
dict_alpha_upper = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
dict_alpha_lower = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
word = str(input())
new_word = []
for i in range(len(word)):
    if word[i].isalpha():
        if word[i].isupper():
            new_idx = dict_alpha_upper.index(word[i]) + 13
            if new_idx >= 26:
                new_idx = new_idx % 25 - 1
            # print(dict_alpha_upper[new_idx])
            new_word.append(dict_alpha_upper[new_idx])
        else:
            new_idx = dict_alpha_lower.index(word[i]) + 13
            if new_idx >= 26:
                new_idx = new_idx % 25 - 1
            # print(dict_alpha_lower[new_idx])
            new_word.append(dict_alpha_lower[new_idx]) 
    else:
        new_word.append(word[i])
        pass

for m in new_word:
    print(m, end='') 