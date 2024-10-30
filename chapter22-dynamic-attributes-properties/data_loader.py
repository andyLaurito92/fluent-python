import json
import os
from pathlib import Path

DATA_PATH = 'data/osconfeed.json'


if __file__:
    DATA_FILE = Path(os.path.abspath(os.path.dirname(__file__))) / DATA_PATH
else:
    print("Assuming that we are in directory named chapter22")
    DATA_FILE = Path(os.getcwd() + DATA_PATH)

data = json.load(open(DATA_FILE))
