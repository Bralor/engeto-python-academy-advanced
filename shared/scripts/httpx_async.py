import time
import asyncio

import httpx


async def ziskej_odpoved_serveru():
    urls = [
        'http://books.toscrape.com/catalogue/a-light-in-the-attic_1000/index.html',
        'http://books.toscrape.com/catalogue/tipping-the-velvet_999/index.html',
        'http://books.toscrape.com/catalogue/soumission_998/index.html',
        'http://books.toscrape.com/catalogue/sharp-objects_997/index.html',
        'http://books.toscrape.com/catalogue/sapiens-a-brief-history-of-humankind_996/index.html',
        'http://books.toscrape.com/catalogue/the-requiem-red_995/index.html',
        'http://books.toscrape.com/catalogue/the-dirty-little-secrets-of-getting-your-dream-job_994/index.html',
        'http://books.toscrape.com/catalogue/the-coming-woman-a-novel-based-on-the-life-of-the-infamous-feminist-victoria-woodhull_993/index.html'
    ]

    async with httpx.AsyncClient() as client:
        requests_ = [client.get(url) for url in urls]
        response = await asyncio.gather(*requests_)


if __name__ == '__main__':
    start = time.perf_counter()
    asyncio.run(ziskej_odpoved_serveru())
    stop = time.perf_counter()
    print(f"Celkem: {stop - start:.2f} vteřin.")
