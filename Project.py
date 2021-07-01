import random
import requests
import pprint



def introduction():
    with open('Python-Course\Pokemon_script.txt', 'r') as file:
        input(file.readline())
        input(file.readline())
        print()
 
    while True:
        gender=str(input('OAK: Are you a BOY or a GIRL?'))
        answer=str(input(f'OAK: Oh so you are a {gender}? Is that correct?').lower())
        if answer== 'yes':
            print('OAK: Oh okay...')
 
            break 
 
    return str(input('OAK: What was your name again?'))
    
name_answer=introduction()
input(f'OAK: Oh I remember now, your name is {name_answer}')
 
def pokemon_options():
 
    while True:
        pokemon1=input('OAK: Which pokemon would you like to choose? Charmander, bulbasaur or squirtle?').lower()
        options=["charmander", "bulbasaur", "squirtle"]
        if pokemon1 in options:
            pokemon_answer=str(input(f'OAK: Oh so you want {pokemon1}? Is that correct?').lower())
            if pokemon_answer== 'yes':
                print(f'OAK: Excellent! Here is your {pokemon1}')
                break
        else:
            print('We don''t have that pokemon, choose again')
 
    input(f'{pokemon1} emerged from the pokeball!')
 
    if pokemon1=="charmander":
        my_pokemon = {
        "pokemon":"charmander",
        "type":"fire",
        "level": 5,
        "hp": 20,
        "max hp":20,
        }
    elif pokemon1=="bulbasaur":
        my_pokemon = {
        "pokemon":"bulbasaur",
        "type":"grass",
        "level": 5,
        "hp": 20,
        "max hp":20
        }
    elif pokemon1=="squirtle":
        my_pokemon = {
        "pokemon":"squirtle",
        "type":"water",
        "level": 5,
        "hp": 2,
        "max hp":20
        }
    return my_pokemon



 
    
a=pokemon_options()
pokedex=[a]
input(f' {a["pokemon"]} was added to the pokedex')
print()
input(pokedex)
print()



def pokemon_api(pokemon_name):
    response = requests.get(f"https://pokeapi.co/api/v2/pokemon-species/{pokemon_name}")
    pokemon_stats = response.json()
    pokemon_description=pokemon_stats["flavor_text_entries"][8]["flavor_text"]
    input()
    print()
    print(pokemon_description)
    print()
    print()
    input()

pokemon_api(pokedex[0]["pokemon"])    

with open('Python-Course\Pokemon_script.txt', 'r') as file:
        input(file.readlines()[2])
        print()
 
 
inventory={
    'Potion': 1,
    'Pokeball': 5,
    'Rare candy': 1
    }
 
wild_pokemon=[{ 
    "pokemon":"pidgey",
    "type":"flying",
    "level": 4,
    "hp": 15,
    "max hp":15
    },
    {"pokemon":"wingull",
    "type":"flying",
    "level": 5,
    "hp": 20,
    "max hp":20
    }]
 
def level_up():
    pokedex[0]["level"]=pokedex[0]["level"]+1
    input(f'{pokedex[0]["pokemon"]} levelled up to Level: {pokedex[0]["level"]}')
    pokedex[0]["max hp"]= pokedex[0]["max hp"]+5
    pokedex[0]["hp"]= pokedex[0]["hp"]+3
    input(pokedex[0])
 
def add_to_pokedex(new_pokemon):
    input(f'{new_pokemon["pokemon"]} was caught!')
    pokedex.append(new_pokemon)
    input(f' {new_pokemon["pokemon"]} was added to the pokedex')
    print()
    print()
    input(pokedex)
    input()

 
def opponent_attack(opponent):
    opponent_moves=[1,2]
    move_result=random.choices(opponent_moves,weights=(2,1),k=1)
    if move_result==[1]:
        input(f'{opponent["pokemon"]} used peck')
        if pokedex[0]["pokemon"]=="Bulbasaur":
            pokedex[0]["hp"]=pokedex[0]["hp"]-10
            input('It is super effective! Bulbasaur lost 10hp!')
            print(f'hp:{pokedex[0]["hp"]}')
            if pokedex[0]["hp"]<=0:
                input(f'{pokedex[0]["pokemon"]} fainted!')
            else:
                input(f'Come on {pokedex[0]["pokemon"]}!') 
        else:
            pokedex[0]["hp"]=pokedex[0]["hp"]-5
            input(f'{pokedex[0]["pokemon"]} lost 5hp!')
            print(f'hp:{pokedex[0]["hp"]}')
            if pokedex[0]["hp"]<=0:
                input(f'{pokedex[0]["pokemon"]} fainted!')
            else:
                input(f'Come on {pokedex[0]["pokemon"]}!')
    else:
        input(f'{opponent["pokemon"]} used protect')
 
def opponent_attack2(opponent):
        input(f'{opponent["pokemon"]} used peck')
        if pokedex[0]["pokemon"]=="bulbasaur":
            pokedex[0]["hp"]=pokedex[0]["hp"]-10
            input('It is super effective! Bulbasaur lost 10hp!')
            print(f'hp:{pokedex[0]["hp"]}')
            if pokedex[0]["hp"]<=0:
                input(f'{pokedex[0]["pokemon"]} fainted!')
            else:
                input(f'Come on {pokedex[0]["pokemon"]}!') 
        else:
            pokedex[0]["hp"]=pokedex[0]["hp"]-5
            input(f'{pokedex[0]["pokemon"]} lost 5hp!')
            print(f'hp:{pokedex[0]["hp"]}')
            if pokedex[0]["hp"]<=0:
                input(f'{pokedex[0]["pokemon"]} fainted!')
            else:
                input(f'Come on {pokedex[0]["pokemon"]}!')
   
def battle_bag_potion(opponent):
    hp_difference=pokedex[0]["max hp"]-pokedex[0]["hp"]
    if inventory["Potion"]==0:
         print('No potions left!')
    elif pokedex[0]["hp"]==pokedex[0]["max hp"]:
         print('HP won''t go any higher!')
    elif hp_difference<10:
        pokedex[0]["hp"]=20
        print(f'HP has been restored to {pokedex[0]["hp"]}')
        inventory["Potion"]=inventory["Potion"]-1
        opponent_attack(opponent)
    else:
        pokedex[0]["hp"]=pokedex[0]["hp"]+10
        print(f'HP has been restored to {pokedex[0]["hp"]}')
        inventory["Potion"]=inventory["Potion"]-1
        opponent_attack(opponent)
 
def battle_bag_pokeball(opponent):
    if inventory["Pokeball"]==0:
        print('No pokeballs left!')
    else:
        input(f'{name_answer} threw a pokeball!')
        inventory["Pokeball"]=inventory["Pokeball"]-1
        pokeball_catch=[1,0]
        result=random.choices(pokeball_catch,weights=(1,1),k=1)
        print(result)
        if result==[1]:
            add_to_pokedex(opponent)
            pokemon_api(opponent["pokemon"])  
        else:
            input(f'{opponent["pokemon"]} escaped the pokeball!')
            opponent_attack(opponent)
 
def battle_switch_pokemon():
    if len(pokedex)==1:
        input('You have no other pokemon!')
    else:
        for item in pokedex:
            print(item["pokemon"])
        while True:
            switch=input('Select the pokemon you wish to switch to').lower()
            if switch==pokedex[1]["pokemon"]:
                pokedex.reverse()
                input(f'Go {switch}!')
                break
            elif switch==pokedex[0]["pokemon"]:
                input('This pokemon has already been selected!')
            else:
                print('error')
 
            
def battle_fight(opponent):
    opponent_moves=[1,2]
    move_result=random.choices(opponent_moves,weights=(1,2),k=1)
    if pokedex[0]["pokemon"]=="pidgey":
        attack=input('Select move: [PECK/PROTECT]').lower()
        if attack=="peck":
            if move_result==[2]:
                input(f'{opponent["pokemon"]} used protect')
                input('Pidgey used peck!')
                input(f'But {opponent["pokemon"]} protected itself!')
            else:
                input('Pidgey used peck!')
                opponent["hp"]=opponent["hp"]-5
                input(f'{opponent["pokemon"]} lost 5hp!')
                input(f'remaining hp: {opponent["hp"]}')
                if opponent["hp"]<=0:
                    input(f'{opponent["pokemon"]} fainted!')
                else:
                    opponent_attack2(opponent)
        if attack=="protect":
            input('Pidgey used protect!')
            if move_result==[2]:
                input(f'{opponent["pokemon"]} used protect')
            else: 
                input(f'{opponent["pokemon"]} used peck')
                input('But Pidgey protected itself!')
    if pokedex[0]["pokemon"]==a["pokemon"]:
        attack=input('Select move: [TACKLE/RECOVER]').lower()
        if attack=="tackle":
            if move_result==[2]:
                input(f'{opponent["pokemon"]} used protect')
                input(f'{pokedex[0]["pokemon"]} used tackle!')
                input(f'But {opponent["pokemon"]} protected itself!')
            else:
                input(f'{pokedex[0]["pokemon"]} used tackle!')
                opponent["hp"]=opponent["hp"]-10
                input(f'{opponent["pokemon"]} lost 10hp!')
                input(f'remaining hp: {opponent["hp"]}')
                if opponent["hp"]<=0:
                    input(f'{opponent["pokemon"]} fainted!')
                else:
                    opponent_attack2(opponent)
        if attack=="recover":
            input(f'{pokedex[0]["pokemon"]} used recover!')
            pokedex[0]["hp"]=pokedex[0]["hp"]+5
            print(f'{pokedex[0]["pokemon"]} recovered HP! HP has been restored to {pokedex[0]["hp"]}')
            opponent_attack(opponent)

def pokemon_battle(opponent):
    while True:
        action=str(input('What do you want to do? [FIGHT/POKEMON/BAG/RUN]').lower())
        if action=='run':
            input('You ran away safely.')            
            break
        elif action== 'bag':
            print(inventory)            
            action_bag=str(input('What would you like to use? [POTION/POKEBALL/RARE CANDY]').lower())
            if action_bag=='potion':
                battle_bag_potion(opponent)
                if pokedex[0]["hp"]<=0:
                    if pokedex[0]["hp"]<=0 and len(pokedex)==1:
                        break
                    elif pokedex[0]["hp"]<=0 and pokedex[1]["hp"]<=0:
                        break
                    else:
                        battle_switch_pokemon()
            elif action_bag=='pokeball':
                battle_bag_pokeball(opponent)
                if pokedex[0]["hp"]<=0:
                    if pokedex[0]["hp"]<=0 and len(pokedex)==1:
                        break
                    elif pokedex[0]["hp"]<=0 and pokedex[1]["hp"]<=0:
                        break
                    else:
                        battle_switch_pokemon()
                elif opponent in pokedex:
                        break
            elif action_bag=='rare candy':
                if inventory["Rare candy"]==0:
                    print('No rare candy left!')
                else:
                    level_up()
                    inventory["Rare candy"]=inventory["Rare candy"]-1
                    opponent_attack(opponent)
                    if pokedex[0]["hp"]<=0:
                        if pokedex[0]["hp"]<=0 and len(pokedex)==1:
                            break
                        elif pokedex[0]["hp"]<=0 and pokedex[1]["hp"]<=0:
                            break
                        else:
                            battle_switch_pokemon()
        elif action== 'pokemon':
            battle_switch_pokemon()
        elif action== 'fight':
            battle_fight(opponent)
            if pokedex[0]["hp"]<=0:
                if pokedex[0]["hp"]<=0 and len(pokedex)==1:
                    break
                elif pokedex[0]["hp"]<=0 and pokedex[1]["hp"]<=0:
                     break
                else:
                    battle_switch_pokemon()
            if opponent["hp"]<=0:
                break
 
input()
with open('Python-Course\Pokemon_script.txt', 'r') as file:
        input(file.readlines()[3])
        print()
pokemon_battle(wild_pokemon[0])

if pokedex[0]["hp"]<=0:
     print('GAME OVER')
else:
    with open('Python-Course\Pokemon_script.txt', 'r') as file:
        input(file.readlines()[4])
        print()
        pokemon_battle(wild_pokemon[1])
    if pokedex[0]["hp"]<=0 and len(pokedex)==1:
        print('GAME OVER')
    elif pokedex[0]["hp"]<=0 and pokedex[1]["hp"]<=0:
        print('GAME OVER')
    else:
        with open('Python-Course\Pokemon_script.txt', 'r') as file:
            input(file.readlines()[5])
            print()