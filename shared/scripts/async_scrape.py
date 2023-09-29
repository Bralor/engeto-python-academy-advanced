import time
import asyncio

import requests
from bs4 import BeautifulSoup


async def skrejpuj_pokemony_par(
        url: str = 'https://pokemondb.net/pokedex/') -> list:
    start = time.perf_counter()

    selekce = ('bulbasaur', 'charmander', 'squirtle', 'butterfree', 'snorlax')
    data = [
        asyncio.create_task(skrejpuj_pokemona(f'{url}{jmeno}'))
        for jmeno in selekce
    ]
    hotove = await asyncio.wait(data)

    stop = time.perf_counter()
    print(f'Trvalo to: {stop - start:.2f} vteřin.')

    return data


async def skrejpuj_pokemona(url: str) -> str:
    response = requests.post(url)

    if response.status_code == 200:
        pokemon_soup = BeautifulSoup(response.text, features='html.parser')
        pokemon_intro = pokemon_soup.find_all('p')
        print(pokemon_intro[0].text)
        return pokemon_intro[0].text
    else:
        raise Exception('Cannot get the server response')


if __name__ == '__main__':
    asyncio.run(skrejpuj_pokemony_par())
