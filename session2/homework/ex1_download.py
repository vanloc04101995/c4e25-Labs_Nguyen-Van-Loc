from urllib.request import urlopen
from bs4 import BeautifulSoup
import pyexcel
from collections import OrderedDict
from youtube_dl import YoutubeDL
url = "https://www.apple.com/itunes/charts/songs/"
conn = urlopen(url)
raw_data = conn.read()
content = raw_data.decode("utf8")
soup =  BeautifulSoup(content,"html.parser")
section = soup.find("section","section chart-grid")
li_list= section.find_all("li")
news_list =[]
for li in li_list:
    numbers = li.strong.string
    name_song = li.h3.a.string
    artists = li.h4.a.string
    song = {
        "STT" : numbers,
        "Name of song": name_song,
        "Artists" : artists
    }
    news_list.append(OrderedDict(song))
    options = {
    'default_search': 'ytsearch', # tell downloader to search instead of directly downloading
    'max_downloads': 1 # Tell downloader to download only the first entry (video)
    }
    dl = YoutubeDL(options)
    dl.download([song['Name of song']+song['Artists']])
