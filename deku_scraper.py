""" This script scrapes your dekudeals.com wishlist
    Need to haves:
        - Game title, price, digital/physical
    Nice to haves:
        - Scrape links to reviews from other websites
        - Links to gameplay vids from youtube (See if we can scrape specific channels)

"""

from lxml import html
from bs4 import BeautifulSoup
import requests
import pandas as pd 
import numpy as np

URL = 'https://www.dekudeals.com/wishlist/46gcmbkm43'
page = requests.get(URL)

results = requests.get(URL)

game_soup = BeautifulSoup(results.text, "html5lib")
price_soup = BeautifulSoup(results.text, "html5lib")

games = [] 
price = []
# discount = [] - This isn't used yet.

game_div = game_soup.find_all('div', 'main')
price_div = price_soup.find_all('div', 'price')

for g in game_div:

    game = g.a.text
    games.append(game.strip())

for p in price_div:
    
    cost = p.text
    price.append(cost.replace('\n',' ').replace('%', '% '))

games_list = pd.DataFrame({
    'Title' : games,
    'Price' : price,
})

print(games_list)