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

# k=input("enter number of pokemons")
# pokemons=[]


# for i in range (0,len(Pokedex.key()))


# for i in range (0,k):

#     combined = combined | poke_finder()






# for p1, types1 in Pokedex.items():
#     for p2, types2 in Pokedex.items():
#         if p1 == p2:
#             continue
        
#         combined = set(types1) | fucntion()   # union

#         if len(combined) > max_types:
#             max_types = len(combined)
#             best_pair = (p1, p2)



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

# Global best result
best_team = []
best_types = set()

def backtrack(pokemon_list, k, idx, current_team, current_types):
    global best_team, best_types
    
    # Base case: if we've chosen k Pokémon
    if len(current_team) == k:
        if len(current_types) > len(best_types):
            best_types = current_types.copy()
            best_team = current_team.copy()
        return
    
    # If we've run out of Pokémon to pick
    if idx == len(pokemon_list):
        return
    
    # --- PRUNING ---
    # Upper bound = current types + all remaining distinct types
    remaining_types = set()
    for i in range(idx, len(pokemon_list)):
        remaining_types.update(pokemon_list[i][1])
    
    if len(current_types) + len(remaining_types) <= len(best_types):
        return  # prune this branch
    
    # Choice 1: take this Pokémon
    name, types = pokemon_list[idx]
    backtrack(
        pokemon_list, k, idx + 1,
        current_team + [name],
        current_types | set(types)
    )
    
    # Choice 2: skip this Pokémon
    backtrack(
        pokemon_list, k, idx + 1,
        current_team,
        current_types
    )

# Ask user for input
k = int(input("Enter maximum number of Pokémon to pick: "))

# Run backtracking
pokemon_list = list(Pokedex.items())
print(pokemon_list)
backtrack(pokemon_list, k, 0, [], set())

# Output result
print("\nBest team:", best_team)
print("Unique abilities:", best_types)
print("Number of unique abilities:", len(best_types))
