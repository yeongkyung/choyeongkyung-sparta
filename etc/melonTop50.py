import requests
from bs4 import BeautifulSoup

headers = {'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
data = requests.get('https://www.melon.com/chart/index.htm',headers=headers)

soup = BeautifulSoup(data.text, 'html.parser')

musics = soup.select('#lst50')

for music in musics:
    rank = music.select_one('td > div > span.rank').text
    title = music.select_one('td > div > div > div.ellipsis.rank01 > span > a').text
    artist = music.select_one('td > div > div > div.ellipsis.rank02 > a').text
    print(rank, title, artist)
