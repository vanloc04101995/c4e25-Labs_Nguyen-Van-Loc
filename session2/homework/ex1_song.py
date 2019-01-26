from urllib.request import urlopen
from bs4 import BeautifulSoup
import pyexcel
from collections import OrderedDict
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
        "Songs'name": name_song,
        "Artists" : artists
    }
    news_list.append(OrderedDict(song))
pyexcel.save_as(records=news_list, dest_file_name="song.xlsx")