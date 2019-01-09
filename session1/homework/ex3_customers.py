import pymongo
from matplotlib import pyplot
uri = "mongodb://admin:admin@ds021182.mlab.com:21182/c4e"

myclient = pymongo.MongoClient(uri)
mydb = myclient["c4e"]
mycollection = mydb["customers"]
eves = 0
ads = 0
wom = 0
for customer in mycollection.find():
    if customer['ref'] == 'events':
        eves += 1
    elif customer['ref'] == 'ads':
        ads += 1
    else:
        wom += 1
print(eves,ads,wom)
# draw
numbersOfPeople = [eves, ads, wom] 
categories = 'Events', 'Advertisements', 'Word of Mouth'
pyplot.pie(numbersOfPeople, labels=categories,autopct='%1.1f%%', shadow=True, explode = [0, 0.1, 0] )
pyplot.title("Percentage of customers")
pyplot.axis("equal")
pyplot.show()