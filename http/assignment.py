import requests
from random import randint

search_term = input('What type of joke do you want to look up? ')

url = 'https://icanhazdadjoke.com/search'
response = requests.get(
    url,
    headers={'Accept': 'application/json'},
    params={
        'term': search_term
    }
)

data = response.json()['results']

if len(data) > 0:
    answer = data[randint(0, len(data) - 1)]
    print(answer['joke'])
else:
    print(f'Can\'t find the joke of: {search_term}!')