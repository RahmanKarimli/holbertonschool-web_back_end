

from pymongo import MongoClient
client = MongoClient()
print(client)

db = client.my_db
school = db.school

# result = school.insert_one({"name": "ayla"})
# print(f"One tutorial: {result.inserted_id}")
# result = school.insert_one({"name": "sevinc"})


for doc in school.find():
    print(doc)





