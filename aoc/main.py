import requests
from pathlib import Path


session_cookie = '' \
                 ' '

def get_input(day: int, year: int):
    Path(f'Day{day}').mkdir(exist_ok=True)
    file_name = f'Day{day}/Input.txt'
    request = requests.get(f'https://adventofcode.com/{year}/day/{day}/input',
                           cookies={"session": session_cookie}).text
    with open(file_name, 'w') as f:
        f.write(request[:-1])

    return request[:-1]