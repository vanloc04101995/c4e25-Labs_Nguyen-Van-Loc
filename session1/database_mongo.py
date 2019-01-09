uri="mongodb://admin:admin@ds021182.mlab.com:21182/c4e"
# conect to data base (mlab)
from pymongo import MongoClient
client = MongoClient(uri)
# Getting a Database
db = client.get_database()
# Getting a Collection
collection = db['posts']
# Creat a Documents
post = {
    'title': 'tôi yêu lập trình',
    'author': 'Nguyễn Văn Lộc',
    'content': '''Biết lập trình từ khá sớm nhưng thật tiếc lại không chú tâm vào nó bởi lúc đó chưa 
                  xác định mình thích cái gì.Đến bây giờ mới bắt đầu có lẽ vẫn là chưa muộn'''
 
}
# Inserting a Document
collection