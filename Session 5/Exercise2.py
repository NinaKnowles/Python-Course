my_pokemon = {
 "pokemon":"Charizard",
 "type":"Fire",
 "level": 55,
}
#print(my_pokemon)
#should be colon not equal sign

#2a

my_stats = {
    "Name":"Nina",
    "Age" : 23,
    "Occupation": "Mechanical Engineer"}

#print(my_stats)

my_stats['Hobby'] = "gaming"

#print(my_stats)

del my_stats['Occupation']
#print(my_stats)

my_stats['Hobby']="reading"
#print(my_stats)

#print(my_stats["Hobby"])

#2b
my_pokemon = {
    "pokemon": "Rapidash",
    "type": "fire",
    "level": "30"
}
#print(my_pokemon)
my_pokemon["move"]="Flame Wheel"
#print(my_pokemon)

n=0
#for value in my_pokemon.values():
    #print(value)

#for keys in my_pokemon.keys():
    #print(keys)


#Extension

my_pokemon = {
    "pokemon": "Rapidash",
    "type": "fire",
    "level": "30"
}
my_pokemon["move"]= ["Flame Wheel", "Agility"]
#print(my_pokemon)

