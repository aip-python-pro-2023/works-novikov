from pokeapi import PokeAPI

def main():
    ditto = PokeAPI.get_pokemon("ditto")
    print("ditto:", ditto)

    heaviest_pokemon = None
    for i, pokemon in enumerate(PokeAPI.get_all(get_full=True)):

        if i == 0 or pokemon.weight > heaviest_pokemon.weight:
            heaviest_pokemon = pokemon

    print("Самый тяжёлый покемон:", heaviest_pokemon)

if __name__ == "__main__":
    main()