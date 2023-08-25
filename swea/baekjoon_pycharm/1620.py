

N, M = map(int, input().split())
my_dict = {}
for i in range(1, N+1):
    pokemon = str(input())
    my_dict[pokemon] = i
    my_dict[i] = pokemon
for _ in range(M):
    quest = input()
    if quest.isdigit():
        print(my_dict[int(quest)])
    else:
        print(my_dict[quest])
'''
26 5
Bulbasaur
Ivysaur
Venusaur
Charmander
Charmeleon
Charizard
Squirtle
Wartortle
Blastoise
Caterpie
Metapod
Butterfree
Weedle
Kakuna
Beedrill
Pidgey
Pidgeotto
Pidgeot
Rattata
Raticate
Spearow
Fearow
Ekans
Arbok
Pikachu
Raichu
25
Raichu
3
Pidgey
Kakuna

'''