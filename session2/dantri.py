# urllib
from urllib.request import urlopen
from bs4 import BeautifulSoup
import pyexcel
from collections import OrderedDict
url = "https://dantri.com.vn/"
# 1.download the page
    # 1.1. Mình với sever là 2 thằng xa lạ, mình phải kết nối vớ n, open connection
conn = urlopen(url)
    # 1.2. Read data
raw_data = conn.read()
    # 1.3 . Decode data
content = raw_data.decode("utf8")
    # print(content)
    # f = open("dantri.html","wb")
    # f.write(raw_data)
    # f.close()
# 2.Find ROI
soup = BeautifulSoup(content, "html.parser")
ul_news = soup.find("ul", "ul1 ulnew")
print(ul_news)
# 3.copy n save
# li_list =  ul_news.find_all("li")
# news_list =[]
# for li in li_list:
#     h4 = li.h4
#     a = h4.a
#     link = url + a["href"]
#     title =  a.string
#     news =OrderedDict({
#         "title" :title,
#         "link" : link
#     })
#     news_list.append(news)
# pyexcel.save_as(records=news_list, dest_file_name="dantri.xlsx")
