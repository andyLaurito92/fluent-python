import asyncio
import sys
from keyword import kwlist

from domainlib import multi_probe


# TLD = Top Level domain

async def main(tld: str) -> None:
    tld = tld.strip('.')
    names = (kw for kw in kwlist if len(kw) <= 4)
    domains = (f'{name}.{tld}'.lower() for name in names)
    print('FOUND\t\tNOT FOUND')
    print('=====\t\t=========')
    async for domain, res in multi_probe(domains):
        ident = '' if res is False else '\t\t'
        print(f'{ident}{domain}')


if __name__ == '__main__':
    if len(sys.argv) == 2:
        asyncio.run(main(sys.argv[1]))
    else:
        print(f'Please specify the top level domain (TLD), example {sys.argv[0]} com.ar')
