import pymongo
client = pymongo.MongoClient("mongodb+srv://gaurav:100200300@cluster0.hs6wjt3.mongodb.net/?retryWrites=true&w=majority")
db = client.test
print(db)

d={ "name": 'gauarv',
    'surname': 'sakpal',
    'email':"gaurav.gmail.com"
}
db1= client["mongotest"]
coll=db1["test"]
coll.insert_one(d)

d1={ "name": 'shambhu',
    'surname': 'jadhav',
    'email':"shambhu.gmail.com"
    }
coll=client["mongotest"]["test"]
coll.insert_one(d1)
