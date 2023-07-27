# 포켓몬 도감
# N: 도감에 수록되어 있는 포켓몬의 개수, M: 내가 맞춰야 하는 문제의 개수
N, M = map(int, input().split())
pokemon_list = []
for i in range(N):
    pokemon = str(input())
    pokemon_list.append(pokemon)
for k in range(M):
    quiz = input()
    if quiz.isalpha():
        print(pokemon_list.index(quiz) + 1)
    else:
        print(pokemon_list[int(quiz)-1])

