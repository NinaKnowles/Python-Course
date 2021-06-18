import requests
import pprint
response = requests.get("https://pokeapi.co/api/v2/pokemon/charmander")
pokemon_stats = response.json()
pprint.pprint(pokemon_stats)

# pokemon_stats.keys()
# pokemon_stats['weight']
# print(pokemon_stats['weight'])


count=0
for ability in pokemon_stats['abilities']:
    print(ability['ability']['name'])
    #count=count+1
    #print(count)

