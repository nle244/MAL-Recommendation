from bs4 import BeautifulSoup
from lxml import html
import requests
from bs4 import BeautifulSoup

link = 'https://myanimelist.net/users.php?lucky=1'
page = requests.get(link).text

soup = BeautifulSoup(page, 'lxml')
user_list = soup.findAll('td', class_ = 'borderClass')
user_names = soup.findAll('div', class_ = 'href')

actors = soup.find_all(class_ ="va-t ar pl4 pr4")

print(actors)