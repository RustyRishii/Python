from time import process_time_ns
from traceback import print_tb
import requests

base_url = "https://pokeapi.co/api/v2/"


def get_pokemon_info(name):
    url = f"{base_url}/pokemon/{name}"
    response = requests.get(url)

    if response.status_code == 200:
        pokemon_data = response.json()
        # print(pokemon_data)
        return pokemon_data
    else:
        print(f"Failed to retrieve data {response.status_code}")


pokemon_name = "Pikachu"
pokemon_info = get_pokemon_info(pokemon_name)

if pokemon_info:
    print()
    print()
    print(f"The name is {pokemon_info['name']}")
    print()
    print(f"The ID is {pokemon_info['id']}")
    print()
    print(f" {pokemon_info['abilities'][0]['slot']}")
    # print(f"The base experience is {pokemon_info['base_experience']}")
    print()
    # print(f"The cries is {pokemon_info['cries']['latest']}")
    print(f"{pokemon_info['is_default']}")
