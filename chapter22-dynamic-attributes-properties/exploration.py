import json
import os
from pathlib import Path

DATA_FILE = Path(os.path.abspath(os.path.dirname(__file__))) / 'data/osconfeed.json'

with open(str(DATA_FILE)) as fp:
    data = json.load(fp)


sorted(data['Schedule'].keys())

for key, value in sorted(data['Schedule'].items()):
    print(f'{len(value):3} {key}')


data['Schedule']['speakers'][-1]['name']

"""
Super annoying to access data like this, right?
"""
