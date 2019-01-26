from pymongo import MongoClient
uri = "mongodb://admin:admin1@ds155490.mlab.com:55490/c4e25"
# 1. connect to mlab sever
client = MongoClient(uri)
# 2. Get a database
db = client.get_database()
# 3. Get a collection
post_collection = db["posts"]
# 4. Create a document
new_post = {
    "title" : "Hom nay troi nhieu may",
    "content" :"Toi o nha code tiep"
}
# 5. insert document
post_collection.insert_one(new_post)
# 6. Lazy loading
# post_list = post_collection.find()
# first_post = post_list[0]
# print(first_post)
# for p in post_list:
#     print(p)
#  exit
client.close()