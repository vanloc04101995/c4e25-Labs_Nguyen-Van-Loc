from urllib.request import urlopen
from bs4 import BeautifulSoup
import pyexcel
from collections import OrderedDict
url = "http://s.cafef.vn/bao-cao-tai-chinh/VNM/IncSta/2017/3/0/0/ket-qua-hoat-dong-kinh-doanh-cong-ty-co-phan-sua-viet-nam.chn"
conn = urlopen(url)
raw_data = conn.read()
content = raw_data.decode("utf8")
soup =  BeautifulSoup(content,"html.parser")
tableHeader = soup.find("table","tblGridData")
tr_header = tableHeader.find_all("tr")
# tableList = soup.find("table","tableContent")
# tr_list = tableList.find_all("tr")
td_header = tr_header.find_all("td")
print(td_header)
# news_list_header =[]


# pyexcel.save_as(records=news_list_header, dest_file_name="song.xlsx")