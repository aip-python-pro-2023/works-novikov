from pokeapi import PokeAPI


ditto = PokeAPI.get_pokemon("ditto")
print("Pokemon Ditto:", ditto)


heaviest_pokemon = None
max_weight = 0

for pokemon in PokeAPI.get_all(get_full=True):
    print(pokemon)
    if pokemon._weight > max_weight:
        max_weight = pokemon._weight
        heaviest_pokemon = pokemon

print("Heaviest Pokemon:", heaviest_pokemon)
