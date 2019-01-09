import pymongo
uri = "mongodb://admin:admin@ds021182.mlab.com:21182/c4e"

myclient = pymongo.MongoClient(uri)
# 2. Get a database
mydb = myclient["c4e"]
#print(mydb.list_collection_names())
mycollection = mydb["posts"]
new_post = {
    "title" : "Tôi yêu lập trình",
}
# 5. insert document
# mycollection.delete_one(new_post)
