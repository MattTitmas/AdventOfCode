import requests
from pathlib import Path


session_cookie = '53616c7465645f5f19eb917ec65266c3a14786c1715903010082dc17c3c1ba95' \
                 'ab62acaac48643de4386e351b7d8144e594056724924bf47a343024f7cc1c210 '

def get_input(day: int, year: int):
    Path(f'Day{day}').mkdir(exist_ok=True)
    file_name = f'Day{day}/Input.txt'
    request = requests.get(f'https://adventofcode.com/{year}/day/{day}/input',
                           cookies={"session": session_cookie}).text
    with open(file_name, 'w') as f:
        f.write(request[:-1])

    return request[:-1]