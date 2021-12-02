import requests
from datetime import date


if __name__ == "__main__":

    # Get session cookie
    with open('cookie.txt', 'rt') as f:
      cookie = f.read()

    # Get today's date and make request
    today = date.today().day
    url = f'https://adventofcode.com/2021/day/{today}/input'
    request = requests.get(url, cookies={'session': cookie})

    # Save to file
    with open(f'input{str(today).zfill(2)}.txt', 'w') as f:
      f.write(request.text)