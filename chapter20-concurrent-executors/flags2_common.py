import argparse
import string
import sys
import time
from collections import Counter
from enum import Enum
from pathlib import Path

DownloadStatus = Enum('DownloadStatus', 'OK NOT_FOUND ERROR')

POP20_CC = ('CN IN US ID BR PK NG BD RU JP '
            'AR MX PH VN ET EG DE IR TR CD').split()

DEFAULT_CONCUR_REQ = 1
MAX_CONCUR_REQ = 1

SERVERS = {
    'REMOTE': 'https://www.fluentpython.com/data/flags',
    'LOCAL': 'http://localhost:8000/flags',
    'DELAY': 'http://localhost:8001/flags',
    'ERROR': 'http://localhost:8002/flags',
    }

DEFAULT_SERVER = 'LOCAL'

DEST_DIR = Path('downloaded')
COUNTRY_CODE_FILE = Path('country_codes.txt')


def save_flag(img: bytes, filename: str) -> None:
    (DEST_DIR / filename).write_bytes(img)


def initial_report(cc_list: list[str],
                   actual_req: int,
                   server_label: str) -> None:
    if len(cc_list) <= 10:
        cc_msg = ', '.join(cc_list)
    else:
        cc_msg = f'from {cc_list[0]} to {cc_list[-1]}'

    print(f'{server_label} site: {SERVERS[server_label]}')
    plural = 's' if len(cc_list) != 1 else ''
    print(f'Searching for {len(cc_list)} flag{plural}: {cc_msg}')
    if actual_req == 1:
        print('1 connection will be used.')
    else:
        print(f'{actual_req} concurrent connections will be used.')
          

def final_report(cc_list: list[str],
                 counter: Counter[DownloadStatus],
                 start_time: float) -> None:
    elapsed = time.perf_counter() - start_time
    print('-' * 20)
    plural = 's' if counter[DownloadStatus.OK] != 1 else ''
    if counter[DownloadStatus.NOT_FOUND]:
        print(f'{counter[DownloadStatus.NOT_FOUND:3} not found.')
    elif counter[DownloadStatus.ERROR]:
        plural = 's' if counter[DownloadStatus.ERROR] != 1 else ''
        print(f'{counter[DownloadStatus.ERROR]:3} error{plural}.')

    print(f'Elapsed time: {elapsed:.2f}s')

