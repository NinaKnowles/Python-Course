#2a

with open('c:/Users/CAMNK3/Python/Week 7/pokemon.txt', 'w') as file:

    file.write("Pikachu")

 

#2b

with open('c:/Users/CAMNK3/Python/Week 7/pokemon.txt', 'a') as file:

    file.write("\nCharizard")

 

#2c

 

with open('c:/Users/CAMNK3/Python/Week 7/pokemon.txt', 'a') as file:

    file.writelines(["\nEvee", "\nsquirtle"])