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

def download_many_sequentially(cc_list: list[str]) -> int:
    for cc in sorted(cc_list):
        download_and_save_flag(cc)
    return len(cc_list)


def download_concurrently_threads(cc_list: list[str]) -> int:
    with futures.ThreadPoolExecutor() as threads:
        res = threads.map(download_and_save_flag, sorted(cc_list))


def download_concurrently_processes(cc_list: list[str]) -> int:
    with futures.ProcessPoolExecutor() as processes:
        res = processes.map(download_and_save_flag, sorted(cc_list))


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
    else:
        main(download_concurrently_processes)
