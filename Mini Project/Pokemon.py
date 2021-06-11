input('OAK: Welcome to the world of Pokemon')
input('OAK: My name is Professor Oak')

while True:
    gender=str(input('OAK: Are you a BOY or a GIRL?'))
    answer=str(input(f'OAK: Oh so you are a {gender}? Is that correct?'))
    if answer== 'yes' or answer== 'YES' or answer== 'Yes' :
        print('OAK: Oh okay...')

        break 

name=str(input('OAK: What was your name again?'))
input(f'OAK: Oh I remember now, your name is {name}')

while True:
    pokemon1=input('OAK: Which pokemon would you like to choose? Charmander, bulbasaur or squirtle?')
    if pokemon1=="charmander" or pokemon1=="Charmander" or pokemon1=="bulbasaur" or pokemon1=="Bulbasaur" or pokemon1=="Squirtle" or pokemon1=="squirtle":
        pokemon_answer=str(input(f'OAK: Oh so you want {pokemon1}? Is that correct?'))
        if pokemon_answer== 'yes' or pokemon_answer== 'YES' or pokemon_answer== 'Yes' :
            print(f'OAK: Excellent! Here is your {pokemon1}')
            break
    else:
        print('We don''t have that pokemon, choose again')

input(f'{pokemon1} emerged from the pokeball!')

if pokemon1=="charmander" or pokemon1=="Charmander":
    my_pokemon = {
    "pokemon":"Charmander",
    "type":"Fire",
    "level": 5,
    "hp": 20
    }
elif pokemon1=="bulbasaur" or pokemon1=="Bulbasaur":
    my_pokemon = {
    "pokemon":"Bulbasaur",
    "type":"Grass",
    "level": 5,
    "hp": 20
    }
elif pokemon1=="Squirtle" or pokemon1=="squirtle":
     my_pokemon = {
    "pokemon":"Squirtle",
    "type":"Water",
    "level": 5,
    "hp": 20
    }

input(my_pokemon)

input('A few hours later, in Virdian forest')
input('A wild Pidgey appeared!')

inventory={
    'Potion': 2,
    'Pokeball': 5,
    'Rare candy': 1
    }


while True:
    action=str(input('What do you want to do? [FIGHT/POKEBALL/BAG/RUN]'))
    if action=='RUN' or action== 'Run' or action== 'Run':
        input('You ran away safely.')
        break
  #  elif action== 'BAG' or action == 'Bag' or action =='bag':