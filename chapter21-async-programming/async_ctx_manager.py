import asyncio
import requests
from collections.abc import Iterator
from collections import defaultdict
from contextlib import asynccontextmanager

# Num of requests to url
stats: defaultdict[str, int] = defaultdict(lambda: 0)

def download_webpage(url: str) -> Iterator[str]:
    response = requests.get(url, stream=True)
    # Reponse from requests allows to iterate over the
    # response in chunks. The below line returns a generator
    yield from response.iter_content(chunk_size=2)
    #return response.text
    

def update_stats(url: str) -> None:
    stats[url] = stats.get(url, 0) + 1
    print(stats)


@asynccontextmanager
async def web_page(url):
    loop = asyncio.get_event_loop()
    data = await loop.run_in_executor(
        None, download_webpage, url)
    yield data
    await loop.run_in_executor(None, update_stats, url)


# Usage example

async def main():
    async with web_page('https://google.com') as web_page_gen_res:
        for chunk in web_page_gen_res:
            print(chunk)
   

if __name__ == '__main__':
    asyncio.run(main())
