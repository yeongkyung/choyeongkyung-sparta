import requests
from bs4 import BeautifulSoup

headers = {'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
data = requests.get('https://www.genie.co.kr/chart/top200?ditc=D&ymd=20200403&hh=23&rtm=N&pg=1',headers=headers)

soup = BeautifulSoup(data.text, 'html.parser')

musics = soup.select('#body-content > div.newest-list > div > table > tbody > tr')

for music in musics:
    rankTag = music.select_one('td.number').text
    rank = music.select_one('td.number > span').text
    title = music.select_one('td.info > a.title.ellipsis').text
    artist = music.select_one('td.info > a.artist.ellipsis').text   
    print(rankTag.rstrip(rank).rstrip(),title.lstrip(),artist)