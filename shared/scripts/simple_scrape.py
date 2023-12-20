import time

import requests
from bs4 import BeautifulSoup


def skrejpuj_pokemony(
        *args, url: str = 'https://pokemondb.net/pokedex/') -> list:
    return [
        skrejpuj_pokemona(f'{url}{jmeno}')
        for jmeno in args
    ]


def skrejpuj_pokemona(url: str) -> str:
    response = requests.post(url)

    if response.status_code == 200:
        pokemon_soup = BeautifulSoup(response.text, features='html.parser')
        pokemon_intro = pokemon_soup.find_all('p')
        print(pokemon_intro[0].text)
        return pokemon_intro[0].text
    else:
        raise Exception('Cannot get the server response')


def main():
    start = time.perf_counter()
    seznam_uvodnich_slov = skrejpuj_pokemony(
            'bulbasaur', 'charmander', 'squirtle', 'butterfree', 'snorlax'
    )
    stop = time.perf_counter()
    print(f'Trvalo to: {stop - start:.2f} vteřin.')


if __name__ == '__main__':
    main()
