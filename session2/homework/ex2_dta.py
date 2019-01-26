from urllib.request import urlopen
from bs4 import BeautifulSoup
import pyexcel
from collections import OrderedDict

url = "http://s.cafef.vn/bao-cao-tai-chinh/VNM/IncSta/2017/3/0/0/ket-qua-hoat-dong-kinh-doanh-cong-ty-co-phan-sua-viet-nam.chn"
conn = urlopen(url)
raw_data = conn.read()
content = raw_data.decode("utf8")
soup =  BeautifulSoup(content,"html.parser")
table = soup.find('table',id='tableContent')
header_data = ['Mục','Quý 4-2016','Quý 1-2017','Quý 2-2017','Quý 3-2017',]
list_data = []
dict_data = {}
tr_list = table.find_all('tr',{"class":["r_item", "r_item_a"]})

for tr in tr_list:
    td_list  = tr.find_all("td")
    for i, td in enumerate(td_list):
        if i < 5: 
            td_data = td.string
            td_data = str(td_data).strip()
            dict_data[header_data[i]] = td_data
    list_data.append(OrderedDict(dict_data))

pyexcel.save_as(records = list_data, dest_file_name  = "vinamilk.xlsx")
    