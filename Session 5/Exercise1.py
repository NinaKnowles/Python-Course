#1a
pokemon= ["Infernape", "Torchic", "Skarmory", "Metagross", "Salamence", "Milotic"]
print(pokemon)

pokemon.insert(3,"Swampert")
print(pokemon)

pokemon.pop(4)
print(pokemon)

pokemon.remove("Milotic")
print(pokemon)

print(pokemon[3])

#1b
my_team=["Landorus", "Weedle", "Spearow", "Pidgey", "Gardevoir"]
print(my_team)

#1c
pokedex= pokemon+my_team
print(pokedex)

#1d
pokedex.insert(2, "Rattata")
print(pokedex)

#1e
pokedex_length=len(pokedex)
print(pokedex_length)

#1f 
n=0
for number in range (pokedex_length):
    print(pokedex[n])
    n=n+1

#1g

if "Charizard" in pokedex:
    print("Charizard is in the pokedex")
else:
    print("Charizard is not in the pokedex")


    