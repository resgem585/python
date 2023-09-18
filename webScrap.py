import requests
from bs4 import BeautifulSoup

url = f'http://soria-goig.com/historia/ermitas/ermitas.htm'

response = requests.get(url)

if response.status_code == 200:

    soup =  BeautifulSoup(response.text, 'html.parser')
    word = 'pueblo'

    if word in soup.get_text().lower():
        print(f'Se encuentra la palabra {word} en la url {url}')
        print(soup.get_text().lower())

else:
    print('Error no se puede acceder a la pagina')