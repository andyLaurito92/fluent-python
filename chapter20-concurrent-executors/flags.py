import sys
import time
from enum import StrEnum
from pathlib import Path
from typing import Callable
from concurrent import futures

import httpx


POP20_CC = ('CN IN US ID BR PK NG BD RU JP '
            'MX PH VN ET EG DE IR TR CD FR').split()

BASE_URL = 'https://www.fluentpython.com/data/flags'
DEST_DIR = Path('downloaded')

def save_flag(img: bytes, filename: str) -> None:
    (DEST_DIR / filename).write_bytes(img)

def get_flag(cc: str) -> bytes:
    url = f'{BASE_URL}/{cc}/{cc}.gif'.lower()
    resp = httpx.get(url, timeout=6.1, follow_redirects=True)
    # If HTTP status is not in 2XX range, raise an exception
    resp.raise_for_status()
    return resp.content

def download_and_save_flag(cc: str) -> None:
    image = get_flag(cc)
    save_flag(image, f'{cc}.gif')
    # Change end character which defaults to \n to space
    # flush=True bc by default, Python output is line buffered!
    # Meaning that Python only displays printed characters AFTER
    # a line break
    print(cc, end=' ', flush=True)
    return f'Ended downloading {cc}'

def download_many_sequentially(cc_list: list[str]) -> int:
    for cc in sorted(cc_list):
        download_and_save_flag(cc)
    return len(cc_list)


# In this method we use Futures, sht that we usually don't see
# as normal users, to understand whats going on behind the curtains
# The method we are using is futures.as_completed. Documentation
# can be found here: https://docs.python.org/3/library/concurrent.futures.html#concurrent.futures.as_completed
# And the implementation can be seen here https://github.com/python/cpython/blob/f85af035c5cb9a981f5e3164425f27cf73231b5f/Lib/concurrent/futures/_base.py#L200
def download_many_with_futures(cc_list: list[str]) -> int:
    # We set max_workers to 3 so we can see slowly the output
    with futures.ThreadPoolExecutor(max_workers=3) as executor:
        to_do: list[futures.Future] = []
        for cc in sorted(cc_list):
            future = executor.submit(download_and_save_flag, cc)
            to_do.append(future)
            print(f'Scheduled for {cc}: {future}')

        #as_completed yield futures as they are completed
        for count, future in enumerate(futures.as_completed(to_do), 1):
            res: str = future.result()
            print(f'{future} result: {res!r}')

    return count


# Both ThreadPoolExecutor and ProcessPoolExecutor implement the
# abstract class https://docs.python.org/3.10/library/concurrent.futures.html#concurrent.futures.Executor
def download_concurrently_threads(cc_list: list[str]) -> int:
    # The executor __exit__ method will call executor.shutdown(await=True),
    # which will block untill all threads are done
    with futures.ThreadPoolExecutor() as threads:
        res = threads.map(download_and_save_flag, sorted(cc_list))

    # If any of the threaded calls raises an exception, that exception
    # is raised here when the implicit next() call inside the list
    # constructor tries to retrieve the corresponding return value
    # from the iterator returned by executor.map
    return len(list(res))


def download_concurrently_processes(cc_list: list[str]) -> int:
    with futures.ProcessPoolExecutor() as processes:
        res = processes.map(download_and_save_flag, sorted(cc_list))

    return len(list(res))


def main(downloader: Callable[[list[str]], int]) -> None:
    DEST_DIR.mkdir(exist_ok=True)
    t0 = time.perf_counter()
    count = downloader(POP20_CC)
    elapsed = time.perf_counter() - t0
    print(f'\n{count} downloads in {elapsed:.2f}s')


if __name__ == '__main__':
    if len(sys.argv) < 2:
        main(download_many_sequentially)
    elif sys.argv[1] == 'threads':
        main(download_concurrently_threads)
    elif sys.argv[1] == 'processes':
        main(download_concurrently_processes)
    else:
        main(download_many_with_futures)
