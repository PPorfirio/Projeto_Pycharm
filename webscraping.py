''' coleta de dados web, ou raspagem web, é uma forma de mineração que permite
a extração de dados de sites da web convertendo-os em informação estruturada para
posterior análise'''
from bs4 import BeautifulSoup
import requests

site = requests.get('https://www.climatempo.com.br/').content
soup = BeautifulSoup(site, 'html.parser')

print(soup.prettify())