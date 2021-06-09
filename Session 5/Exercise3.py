my_bag={}  #need to include equal sign and empty brackets
my_bag["item"]="potion" #needs to be equal sign not colon

#3a

pokemon_party={}

#3b
pokemon_party["pokemon"]="Bulbasaur"
pokemon_party["type"]="Grass"
pokemon_party["level"]="5"
print(pokemon_party)

#3c
pokemon_party["moves"]=["Vine whip", "razor leaf", "growl", "cut"]

#3d
pokemon_party["level"]="10"

#3e 

if "cut" in pokemon_party["moves"]:
    print("Cut move exists")