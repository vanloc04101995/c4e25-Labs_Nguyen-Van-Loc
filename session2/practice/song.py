from urllib.request import urlopen
from bs4 import BeautifulSoup
import pyexcel
from collections import OrderedDict

url = "https://mp3.zing.vn/top100/Electronic-Dance/IWZ9Z09A.html"
client = urlopen(url)
raw_data = client.read()
content = raw_data.decode("utf8")
soup = BeautifulSoup(content,"html.parser")
div_list = soup.find("div","table-body")
# ul_list = div_list.find("ul")
# print(ul_list)
li_list = div_list.find_all("li")
print(li_list_add)
# news_list =[]
# for li in li_list :
#     a = li.div.a
#     number = li.span.string
#     nameOfsong = li.div.h3.a.string
#     artis = li.div.div.div.h4.string
#     link = url + a["href"]
#     song = OrderedDict({
#         "STT" :number,
#         "Name Of Song" : nameOfsong,
#         "artis" : artis ,
#         "Link" : link
#     })
#     news_list.append(song)
# pyexcel.save_as(records=news_list, dest_file_name="mp3zing.xlsx")

