Pokedex = {
"Pikachu": ("Electric",),
"Charizard": ("Fire", "Flying"),
"Lapras": ("Water", "Ice"),
"Machamp": ("Fighting",),
"Mewtwo": ("Psychic", "Fighting"),
"Hoopa": ("Psychic", "Ghost", "Dark"),
"Lugia": ("Psychic", "Flying", "Water"),
"Squirtle": ("Water",),
"Gengar": ("Ghost", "Poison"),
"Onix": ("Rock", "Ground")
}


Pokedex = {
    "Pikachu": ("Electric",),
    "Charizard": ("Fire", "Flying"),
    "Lapras": ("Water", "Ice"),
    "Machamp": ("Fighting",),
    "Mewtwo": ("Psychic", "Fighting"),
    "Hoopa": ("Psychic", "Ghost", "Dark"),
    "Lugia": ("Psychic", "Flying", "Water"),
    "Squirtle": ("Water",),
    "Gengar": ("Ghost", "Poison"),
    "Onix": ("Rock", "Ground")
}


best_team = []
best_types = set()

def backtrack(pokemon_list, k, idx, current_team, current_types):
    global best_team, best_types
    
    
    if len(current_team) == k:
        if len(current_types) > len(best_types):
            best_types = current_types.copy()
            best_team = current_team.copy()
        return
    
   
    if idx == len(pokemon_list):
        return
    
    
    remaining_types = set()
    for i in range(idx, len(pokemon_list)):
        remaining_types.update(pokemon_list[i][1])
    
    if len(current_types) + len(remaining_types) <= len(best_types):
        return  
    
    #include path
    name, types = pokemon_list[idx]
    backtrack(
        pokemon_list, k, idx + 1,
        current_team + [name],
        current_types | set(types)
    )
    
    #exlude path
    backtrack(
        pokemon_list, k, idx + 1,
        current_team,
        current_types
    )

k = int(input("Enter maximum number of Pokémon to pick: "))

pokemon_list = list(Pokedex.items())
print(pokemon_list)
backtrack(pokemon_list, k, 0, [], set())
print("\nBest team:", best_team)
print("Unique abilities:", best_types)
print("Number of unique abilities:", len(best_types))
