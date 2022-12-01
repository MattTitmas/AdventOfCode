import os
from pathlib import Path

import requests
from dotenv import load_dotenv

load_dotenv()
session_cookie = os.getenv('SESSION_COOKIE')


def get_input(day: int, year: int):
    Path(f'{year}/Day{day}').mkdir(exist_ok=True)
    if not (os.path.exists(f'{year}/Day{day}/Input.txt')):
        file_name = f'{year}/Day{day}/Input.txt'
        response = requests.get(f'https://adventofcode.com/{year}/day/{day}/input',
                                cookies={"session": session_cookie})
        if response.ok:
            with open(file_name, 'w') as f:
                f.write(response.text[:-1])

            return response.text[:-1]
        else:
            raise RuntimeError(f"Request failed, code: {response.status_code}, message: {response.content}")
    else:
        with open(f'{year}/Day{day}/Input.txt', 'r') as f:
            return f.read()
