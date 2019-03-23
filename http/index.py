import requests

# url = 'http://www.google.com'
url = 'https://icanhazdadjoke.com/search'
response = requests.get(
    url,
    headers={'Accept': 'application/json'},
    params={
        'search': 'dad'
    }
)

# print(f'Your request to {url} came back w/ a status code {response.status_code}')
# print(response.text)
print(response.json()['results'])